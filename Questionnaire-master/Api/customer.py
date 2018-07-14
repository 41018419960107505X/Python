"""
# 客户接口
"""
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

from Questionnaire.settings import DOMAIN
from Question.models import *
from Api.resources import Resource
from Api.utils import *
from Api.decorators import userinfo_required, customer_required, superuser_required


# 问卷资源
class CustomerQuestionnaireResource(Resource):

    @customer_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        state = data.get('state', False)
        limit = abs(int(data.get('limit', 15)))
        start_id = data.get('start_id', False)
        title = data.get('title', False)
        create_date = data.get('create_date', False)
        with_detail = data.get('with_detail', False)
        page = abs(int(data.get('page', 1)))

        Qs = []
        if state:
            state = [int(state)]
        else:
            state = [0, 1, 2, 3, 4]
        Qs.append(Q(state__in=state))

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

        Qs.append(Q(customer=request.user.customer))

        if limit > 50:
            limit = 50
        all_objs = Questionnaire.objects.filter(*Qs)
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
                obj_dict['comments'] = [{
                    'id': item.id,
                    'create_date': datetime.strftime(item.create_date, '%Y-%m-%d'),
                    'comment': item.comment
                } for item in obj.questionnairecomment_set.all()]
                obj_dict['suggests'] = [
                    {
                        "comment": item.comment,
                        "create_date": item.create_date.strftime('%Y-%m-%d')
                    }
                    for item in obj.questionnairesuggest_set.all()
                ]
            # 将问卷添加到问卷列表中
            data.append(obj_dict)

        return json_response({
            'pages': pages,
            'objs': data
        })

    @atomic
    @customer_required
    def put(self, request, *args, **kwargs):
        # 获取请求数据
        data = request.PUT
        # 创建问卷对象
        questionnaire = Questionnaire()
        # 属性赋值
        questionnaire.customer = request.user.customer
        questionnaire.title = data.get('title', '标题')
        # 特殊处理 创建时间使用当前时间
        questionnaire.create_date = datetime.now()
        # 特殊处理 截止时间
        try:
            # 获取截止时间字符串
            deadline_str = data.get('deadline', "")
            # 把时间字符串转化为时间对象
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
        except Exception as e:
            # 如果获取截止时间失败,那么使用当前时间加上10天
            deadline = datetime.now()+timedelta(days=10)

        questionnaire.deadline = deadline
        # 特殊处理 问卷创建时,状态为草稿
        questionnaire.state = 0
        # 特殊处理 默认问卷数量为1份
        questionnaire.quantity = int(data.get('quantity', 1))
        questionnaire.free_count = int(data.get('quantity', 1))
        questionnaire.save()
        return json_response({
            "id": questionnaire.id
        })

    @atomic
    @customer_required
    def post(self, request, *args, **kwargs):
        data = request.POST
        questionnaire_id = int(data.get('questionnaire_id', 0))
        try:
            questionnaire = Questionnaire.objects.get(
                id=questionnaire_id, customer=request.user.customer, state__in=[0, 2, 3])
        except Exception as e:
            return params_error({
                'questionnaire_id': "找不到对应的问卷,或者问卷不可修改"
            })
        questionnaire.title = data.get('title', '标题')
        # 特殊处理 截止时间
        try:
            # 获取截止时间字符串
            deadline_str = data.get('deadline', "")
            # 把时间字符串转化为时间对象
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
        except Exception as e:
            # 如果获取截止时间失败,那么使用当前时间加上10天
            deadline = datetime.now()+timedelta(days=10)
        questionnaire.deadline = deadline

        state = int(data.get('state', 0))
        if state not in [0, 1]:
            return params_error({
                'state': '状态不合法'
            })
        # 特殊state
        questionnaire.state = state

        questionnaire.quantity = int(data.get('quantity', 1))
        questionnaire.free_count = int(data.get('quantity', 1))
        questionnaire.save()

        return json_response({
            "msg": '更新成功'
        })

    @customer_required
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        ids = data.get('ids', [])
        objs = Questionnaire.objects.filter(
            id__in=ids, customer=request.user.customer, state__in=[0, 2, 3])
        deleted_ids = [obj.id for obj in objs]
        objs.delete()
        return json_response({
            'deleted_ids': deleted_ids
        })


class CustomerQuestionResource(Resource):
    @atomic
    @customer_required
    def put(self, request, *args, **kwargs):
        data = request.PUT
        questionnaire_id = data.get('questionnaire_id', 0)
        questionnaire_exists = Questionnaire.objects.filter(id=questionnaire_id,
                                                            customer=request.user.customer, state__in=[0, 2, 3])
        if questionnaire_exists:
            questionnaire = questionnaire_exists[0]
        else:
            return params_error({
                'questionnaire_id': '找不到问卷,或者问卷不可修改'
            })
        # 添加问题
        question = Question()
        question.questionnaire = questionnaire
        question.title = data.get('title', '题纲')
        question.category = data.get('category', 'radio')
        question.index = int(data.get('index', 0))
        question.save()
        # 修改问卷状态
        questionnaire.state = 0
        questionnaire.save()
        # 添加问题选项
        # items=['aaaa','bbbb','cccc','ddddd']
        items = data.get('items', [])

        for item in items:
            question_item = QuestionItem()
            question_item.question = question
            question_item.content = item.get('content', '')
            question_item.save()

        return json_response({
            'id': question.id
        })

    @atomic
    @customer_required
    def post(self, request, *args, **kwargs):
        data = request.POST
        question_id = data.get('id', 0)
        # 判断需要修改的问题是否存在
        question_exits = Question.objects.filter(id=question_id, questionnaire__state__in=[
            0, 2, 3], questionnaire__customer=request.user.customer)
        if not question_exits:
            return params_error({
                'id': "该问题找不到,或者该问题所在问卷无法修改"
            })
        # 更新问题的属性
        question = question_exits[0]
        question.title = data.get('title', '题纲')
        question.category = data.get('category', 'radio')
        question.index = int(data.get('index', 0))
        question.save()
        # 更新问题所在问卷的状态
        questionnaire = question.questionnaire
        questionnaire.state = 0
        questionnaire.save()

        items = data.get('items', [])
        question.questionitem_set.all().delete()
        for item in items:
            question_item = QuestionItem()
            question_item.question = question
            question_item.content = item.get('content', '')
            question_item.save()

        return json_response({
            'msg': '更新成功'
        })

    @atomic
    @customer_required
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        ids = data.get('ids', [])
        objs = Question.objects.filter(id__in=ids, questionnaire__state__in=[
            0, 2, 3], questionnaire__customer=request.user.customer)

        deleted_ids = [obj.id for obj in objs]

        questionnaire_set = set()
        for obj in objs:
            questionnaire_set.add(obj.questionnaire)

        for questionnaire in questionnaire_set:
            questionnaire.state = 0
            questionnaire.save()
        objs.delete()
        return json_response({
            'deleted_ids': deleted_ids
        })


class CustomerQuestionnaireStateResource(Resource):
    @atomic
    @customer_required
    def put(self, request, *args, **kwargs):
        data = request.PUT
        questionnaire_id = data.get('questionnaire_id', 0)
        questionnaire_exits = Questionnaire.objects.filter(
            id=questionnaire_id, customer=request.user.customer, state=3)
        if not questionnaire_exits:
            return params_error({
                'questionnaire_id': '问卷找不到,或者该问卷还未通过审核'
            })
        questionnaire = questionnaire_exits[0]
        questionnaire.state = 4
        questionnaire.save()
        return json_response({
            'state': "发布成功"
        })


class CustomerQuestionIndexResource(Resource):
    @atomic
    @customer_required
    def post(self, request, *args, **kwargs):
        data = request.POST
        questionnaire_exist = Questionnaire.objects.filter(id=data.get(
            'questionnaire_id', 0), state__in=[0, 2, 3], customer=request.user.customer)
        if not questionnaire_exist:
            return params_error({
                'questionnaire_id': "问卷不存在或者问卷不可修改"
            })
        questionnaire = questionnaire_exist[0]
        question_exist = Question.objects.filter(
            questionnaire=questionnaire, id=data.get('id', 0))
        if not question_exist:
            return params_error({
                'question_id': '问题不存在或者问题不可修改'
            })
        question = question_exist[0]
        index = int(data.get('index', 0))
        questionnaire.state = 0
        questionnaire.save()
        question.index = index
        question.save()
        return json_response({
            'msg': '更新成功'
        })


class WalletResource(Resource):
    # 获取钱包信息
    @customer_required
    def get(self, request, *args, **kwargs):
        wallet = Wallet.objects.get(customer__user=request.user)
        result = {
            "balance": wallet.balance
        }
        return json_response(result)

    # 获取充值二维码
    @customer_required
    @atomic
    def put(self, request, *args, **kwargs):
        data = request.PUT
        try:
            amount = abs(int(data.get('amount', 0)))
            if amount == 0:
                raise Exception('金额不合法')
        except Exception:
            return params_error({
                "amount": "金额不合法"
            })
        payment = data.get('payment', 'alipay')
        # 保存支付记录
        flow = WalletFlow()
        flow.amount = amount
        flow.payment = payment
        flow.wallet = request.user.customer.wallet
        flow.done = False
        flow.reason="扫码支付"
        flow.save()
        qrcode = create_qrcode(
            '{domain}/api/v1/paymentback?amount={amount}&payment={payment}&flow_id={flow_id}'.format(domain=DOMAIN,amount=amount, payment=payment, flow_id=flow.id))
        return json_response({
            "qrcode":  qrcode
        })


class WalletFlowResource(Resource):
    # 获取历史记录
    @customer_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        direction = int(data.get('direction', 0))
        limit = abs(int(data.get('limit', 15)))
        start_id = data.get('start_id', False)
        create_date = data.get('create_date', False)
        page = abs(int(data.get('page', 1)))

        Qs = [Q(wallet__customer__user=request.user), Q(done=True)]
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
        all_objs = WalletFlow.objects.filter(*Qs)
        pages = math.ceil(all_objs.count()/limit) or 1
        if page > pages:
            page = pages
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]

        result = {
            "pages": pages,
            "objs": [{
                "id": obj.id,
                "amount": obj.amount,
                "reason": obj.reason,
                "create_date": datetime.strftime(obj.create_date, '%Y-%m-%d %H:%M')
            } for obj in objs]
        }
        return json_response(result)
