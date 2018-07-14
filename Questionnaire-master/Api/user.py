import random
import json
import math
from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.db.transaction import atomic
from django.db.models import Q
from django.utils import timezone

from Question.models import *
from Api.resources import Resource
from Api.utils import *
from Api.decorators import userinfo_required, customer_required, superuser_required

# 问卷资源
class UserQuestionnaireResource(Resource):
    @userinfo_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        limit = abs(int(data.get('limit', 15)))
        start_id = data.get('start_id', False)
        title = data.get('title', False)
        create_date = data.get('create_date', False)
        with_detail = data.get('with_detail', False)
        page = abs(int(data.get('page', 1)))

        Qs = [Q(state=4), Q(deadline__gte=datetime.now()), Q(free_count__gt=0)]
        if start_id:
            start_id = int(start_id)
        else:
            start_id = 0
        Qs.append(Q(id__gt=start_id))

        if title:
            Qs.append(Q(title__contains=title))

        if create_date:
            create_date = datetime.strptime(create_date, '%Y-%m-%d')
            Qs.append(Q(create_date__gt=create_date))

        if limit > 50:
            limit = 50
        # 排除已参与的问卷
        joined = Answer.objects.filter(userinfo=request.user.userinfo)
        joined_ids = [obj.questionnaire.id for obj in joined]
        all_objs = Questionnaire.objects.filter(*Qs).exclude(id__in=joined_ids)
        pages = math.ceil(all_objs.count()/limit) or 1
        if page > pages:
            page = pages
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]

        data = []
        for obj in objs:
            # 构建单个问卷信息
            obj_dict = dict()
            obj_dict['id'] = obj.id
            obj_dict['title'] = obj.title
            obj_dict['create_date'] = datetime.strftime(
                obj.create_date, "%Y-%m-%d")
            obj_dict['deadline'] = datetime.strftime(obj.deadline, "%Y-%m-%d")
            obj_dict['state'] = obj.state
            obj_dict['quantity'] = obj.quantity
            obj_dict['free_count'] = obj.free_count
            obj_dict['customer'] = {
                "id": obj.customer.id,
                "name": obj.customer.name
            }
            if with_detail in ['true', True]:
                # 构建问卷下的问题
                obj_dict['questions'] = []
                for question in obj.question_set.all().order_by('index'):
                    # 构建单个问题
                    question_dict = dict()
                    question_dict['id'] = question.id
                    question_dict['title'] = question.title
                    question_dict['category'] = question.category
                    question_dict['index'] = question.index
                    # 构建问题选项
                    question_dict['items'] = [{
                        "id": item.id,
                        "content": item.content
                    } for item in question.questionitem_set.all()]
                    # 将问题添加到问卷的问题列表中
                    obj_dict['questions'].append(question_dict)
            # 将问卷添加到问卷列表中
            data.append(obj_dict)

        return json_response({
            'pages': pages,
            'objs': data
        })


class JoinQuestionnaireResource(Resource):
    @atomic
    @userinfo_required
    def put(self, request, *args, **kwargs):
        data = request.PUT
        questionnaire_id = data.get('questionnaire_id', 0)
        # 找出要参与的问卷
        questionnaire_exits = Questionnaire.objects.filter(
            id=questionnaire_id, state=4)
        if not questionnaire_exits:
            return params_error({
                'questionnaire_id': '当前问卷不存在'
            })

        # 判断是否已经参与了该问卷
        questionnaire = questionnaire_exits[0]
        has_joined = Answer.objects.filter(
            userinfo=request.user.userinfo, questionnaire=questionnaire)
        if has_joined:
            return params_error({
                'questionnaire_id': '已经参与了该问卷调查'
            })
        # 判断参与问卷的人数是否已满
        has_joined_count = Answer.objects.filter(
            questionnaire=questionnaire).count()
        if questionnaire.quantity <= has_joined_count:
            return params_error({
                'questionnaire_id': '该问卷参与人数已满'
            })
        # 判断问卷是否已经结束
        #  datetime.now() 不带时区 而从数据库中读取出来的时间是带时区的所以不能直接比较
        # 要使用django.utils timezone.now()
        if questionnaire.deadline < timezone.now():
            return params_error({
                'questionnaire_id': '该问卷已结束'
            })
        # 创建参与信息
        answer = Answer()
        answer.userinfo = request.user.userinfo
        answer.questionnaire = questionnaire
        answer.create_date = datetime.now()
        answer.is_done = False
        answer.save()
        # 更新可用问卷数量
        questionnaire.free_count = questionnaire.free_count-1
        questionnaire.save()

        return json_response({
            'id': answer.id
        })

    @atomic
    @userinfo_required
    def post(self, request, *args, **kwargs):
        data = request.POST
        questionnaire_id = data.get('questionnaire_id', 0)
        answer_exist = Answer.objects.filter(
            questionnaire__id=questionnaire_id, userinfo=request.user.userinfo)
        if not answer_exist:
            return params_error({
                "questionnaire_id": "问卷不存在"
            })
        answer = answer_exist[0]
        answer.is_done = True
        answer.save()
        # 增加用户积分
        Point.update_point(request.user.userinfo, 10, '提交问卷')
        return json_response({
            "msg": "更新成功"
        })

    @atomic
    @userinfo_required
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        ids = data.get('ids', [])
        objs = Answer.objects.filter(
            id__in=ids, userinfo=request.user.userinfo, is_done=False)
        deleted_ids = [obj.id for obj in objs]
        # 更新问卷可用数量
        for obj in objs:
            questionnaire = obj.questionnaire
            questionnaire.free_count = questionnaire.free_count+1
            questionnaire.save()
            # 删除用户选择该问卷的所有选项
            AnswerItem.objects.filter(userinfo=request.user.userinfo,item__question__questionnaire=questionnaire).delete()
        objs.delete()
        return json_response({
            'deleted_ids': deleted_ids
        })

    @userinfo_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        limit = abs(int(data.get('limit', 10)))
        start_id = int(data.get('start_id', 0))
        is_done = data.get('is_done', False)
        if is_done in ['true', True]:
            is_done = True
        else:
            is_done = False
        page = int(data.get('page', 1))
        all_objs = Answer.objects.filter(
            id__gt=start_id, userinfo=request.user.userinfo, is_done=is_done)
        count = all_objs.count()
        pages = math.ceil(count/limit) or 1
        if page > pages:
            page = page
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]
        result = {
            'pages': pages,
        }
        data = []
        for obj in objs:
            answer_dict = dict()
            answer_dict['id'] = obj.id
            answer_dict['create_date'] = datetime.strftime(
                obj.create_date, '%Y-%m-%d')
            answer_dict['is_done'] = obj.is_done
            answer_dict['questionnaire'] = {
                'id': obj.questionnaire.id,
                'title': obj.questionnaire.title
            }
            data.append(answer_dict)
        result['objs'] = data
        return json_response(result)


class AnswerQuestionnaireResource(Resource):

    @atomic
    @userinfo_required
    def put(self, request, *args, **kwargs):
        data = request.PUT
        userinfo = request.user.userinfo
        item_id = data.get('item_id', 1)
        item = QuestionItem.objects.get(id=item_id)
        if Answer.objects.filter(is_done=False, questionnaire=item.question.questionnaire, userinfo=userinfo).count() == 0:
            return params_error({
                "item_id": "不可提交该选项"
            })
        question = item.question
        if question.category == 'radio':
            AnswerItem.objects.filter(
                userinfo=userinfo, item__question=item.question).delete()
            answer_item = AnswerItem()
            answer_item.item = item
            answer_item.userinfo = userinfo
            answer_item.save()
        else:
            if AnswerItem.objects.filter(userinfo=userinfo, item=item).count() == 0:
                answer_item = AnswerItem()
                answer_item.item = item
                answer_item.userinfo = userinfo
                answer_item.save()
        return json_response({
            "msg": "选择成功"
        })

    @atomic
    @userinfo_required
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        item_id = data.get('item_id', 0)
        userinfo = request.user.userinfo
        item = QuestionItem.objects.get(id=item_id)
        if Answer.objects.filter(questionnaire=item.question.questionnaire, is_done=True, userinfo=userinfo):
            return params_error({
                "item_id": "不可删除该选项"
            })
        AnswerItem.objects.filter(
            item=item, userinfo=userinfo).delete()
        return json_response({
            "msg": "移除成功"
        })

    @userinfo_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        questionnaire_id = data.get('questionnaire_id', 0)
        has_joined = Answer.objects.filter(
            userinfo=request.user.userinfo, questionnaire__id=questionnaire_id)
        if not has_joined:
            return params_error({
                'questionnaire_id': "没有相关信息"
            })
        questionnaire = Questionnaire.objects.get(id=questionnaire_id)

        data = dict()
        data['id'] = questionnaire.id
        data['title'] = questionnaire.title
        data['customer'] = {
            'name': questionnaire.customer.name
        }
        data['questions'] = []
        for question in questionnaire.question_set.all():
            question_dict = dict()
            question_dict['id'] = question.id
            question_dict['title'] = question.title
            question_dict['index'] = question.index
            question_dict['category'] = question.category

            answers_ids = [
                obj.item.id for obj in AnswerItem.objects.filter(item__question=question,userinfo=request.user.userinfo)
            ]
            question_dict['items'] = [
                {
                    "id": obj.id,
                    "content": obj.content,
                    "active": obj.id in answers_ids
                }
                for obj in question.questionitem_set.all()
            ]
            data['questions'].append(question_dict)

        return json_response(data)


class UserPointResource(Resource):
    @userinfo_required
    def get(self, request, *args, **kwargs):
        userinfo = request.user.userinfo
        data = request.GET
        direction = int(data.get('direction', 0))
        limit = abs(int(data.get('limit', 15)))
        start_id = data.get('start_id', False)
        create_date = data.get('create_date', False)
        page = abs(int(data.get('page', 1)))

        Qs = [Q(point__userinfo=userinfo)]
        if direction == 0:
            direction = False
        else:
            direction = True
        Qs.append(Q(direction=direction))

        if start_id:
            start_id = int(start_id)
        else:
            start_id = 0
        Qs.append(Q(id__gt=start_id))

        if create_date:
            create_date = datetime.strptime(create_date, '%Y-%m-%d')
            Qs.append(Q(datetime__gt=create_date))

        if limit > 50:
            limit = 50
        all_objs = PointHistory.objects.filter(*Qs)
        pages = math.ceil(all_objs.count()/limit) or 1
        if page > pages:
            page = pages
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]
        point = userinfo.point
        result = {
            "balance": point.balance,
            "pages": pages,
            "objs": [{
                "id": obj.id,
                "quantity": obj.quantity,
                "reason": obj.reason,
                "create_date": datetime.strftime(obj.create_date, '%Y-%m-%d %H:%M')
            } for obj in objs]
        }
        return json_response(result)
