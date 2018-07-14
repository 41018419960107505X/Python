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


# 获取注册码
class ReigstCodeResource(Resource):
    def get(self, request, *args, **kwargs):
        regist_code = random.randint(10000, 100000)
        request.session['regist_code'] = regist_code
        return json_response({
            'regist_code': regist_code
        })


# 用户信息
class UserResource(Resource):
    # 获取用户信息
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            # 判断是否是普通用户
            if hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                # 构建json字典
                data = dict()
                data['user'] = user.id
                data['age'] = getattr(userinfo, 'age', '')
                data['name'] = getattr(userinfo, 'name', '')
                data['gender'] = getattr(userinfo, 'gender', '')
                data['phone'] = getattr(userinfo, 'phone', '')
                data['email'] = getattr(userinfo, 'email', '')
                data['address'] = getattr(userinfo, 'address', '')
                if userinfo.birthday:
                    data['birthday'] = userinfo.birthday.strftime("%Y-%m-%d")
                else:
                    data['birthday'] = datetime.now().strftime("%Y-%m-%d")
                data['qq'] = getattr(userinfo, 'qq', '')
                data['wechat'] = getattr(userinfo, 'wechat', '')
                data['job'] = getattr(userinfo, 'job', '')
                data['salary'] = getattr(userinfo, 'salary', '')
                # 用json把data转化成字符串,返回给客户端
                return json_response(data)
            # 判断是否是客户
            elif hasattr(user, 'customer'):
                customer = user.customer
                # 构建json字典
                data = dict()
                data['user'] = user.id
                data['name'] = getattr(customer, 'name', '')
                data['email'] = getattr(customer, 'email', '')
                data['company'] = getattr(customer, 'company', '')
                data['address'] = getattr(customer, 'address', '')
                data['phone'] = getattr(customer, 'phone', '')
                data['mobile'] = getattr(customer, 'mobile', '')
                data['qq'] = getattr(customer, 'qq', '')
                data['wechat'] = getattr(customer, 'wechat', '')
                data['web'] = getattr(customer, 'web', '')
                data['industry'] = getattr(customer, 'industry', '')
                data['description'] = getattr(customer, 'description', '')
                # 用json把data转化称字符串,返回给客户端
                return json_response(data)
            else:
                # 没有相关用户信息,返回空
                return json_response({})
        # 用户未登录,不允许查看信息
        return not_authenticated()

    # 注册用户
    def put(self, request, *args, **kwargs):
        data = request.PUT
        username = data.get('username', '')
        password = data.get('password', '')
        regist_code = data.get('regist_code', '')
        session_regist_code = request.session.get('regist_code', 1111111)
        category = data.get('category', 'userinfo')
        ensure_password = data.get('ensure_password', '')

        # 构建错误信息字典
        errors = dict()
        if not username:
            errors['username'] = '没有提供用户名'
        elif User.objects.filter(username=username):
            errors['username'] = '用户名已存在'
        if len(password) < 6:
            errors['password'] = '密码长度不够'
        if password != ensure_password:
            errors['ensure_password'] = '密码不一样'
        if regist_code != str(session_regist_code):
            errors['regist_code'] = '验证码不对'
        if errors:
            return params_error(errors)
        user = User()
        user.username = username
        # 设置密码
        user.set_password(password)
        user.save()
        # 根据用户类型,创建普通用户或者客户
        if category == 'userinfo':
            userinfo = UserInfo()
            userinfo.user = user
            userinfo.name = '姓名'
            userinfo.save()
        else:
            customer = Customer()
            customer.name = '客户名称'
            customer.user = user
            customer.save()
        login(request, user)
        return json_response({
            "id": user.id
        })

    # 更新用户
    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        if user.is_authenticated:
            # 判断是否是普通用户
            if hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                userinfo.name = data.get('name', '姓名')
                userinfo.age = data.get('age', '')
                userinfo.gender = data.get('gender', '')
                userinfo.phone = data.get('phone', '')
                userinfo.email = data.get('email', '')
                userinfo.address = data.get('address', '')

                # 时间特殊处理
                try:
                    birthday = datetime.strptime(
                        data.get('birthday', '2018-01-01'), "%Y-%m-%d")
                except Exception as e:
                    birthday = datetime.now()

                userinfo.birthday = birthday

                userinfo.qq = data.get('qq', '')
                userinfo.wechat = data.get('wechat', '')
                userinfo.job = data.get('job', '')
                userinfo.salary = data.get('salary', '')
                userinfo.save()
            # 判断是否是客户
            elif hasattr(user, 'customer'):
                customer = user.customer
                customer.name = data.get('name', '客户名称')
                customer.email = data.get('email', '')
                customer.company = data.get('company', '')
                customer.address = data.get('address', '')
                customer.phone = data.get('phone', '')
                customer.mobile = data.get('mobile', '')
                customer.qq = data.get('qq', '')
                customer.wechat = data.get('wechat', '')
                customer.web = data.get('web', '')
                customer.industry = data.get('industry', '')
                customer.description = data.get('description', '')
                customer.save()
            return json_response({
                'msg': '更新成功'
            })
        return not_authenticated()


# 用户登录与退出
class SessionResource(Resource):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return json_response({
                'msg': '已经登录'
            })
        return not_authenticated()

    def put(self, request, *args, **kwargs):
        data = request.PUT
        username = data.get('username', '')
        password = data.get('password', '')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return json_response({
                'msg': '登录成功'
            })
        return params_error({
            'msg': '用户名或密码错误'
        })

    def delete(self, request, *args, **kwargs):
        logout(request)
        return json_response({
            'msg': '退出成功'
        })


# 问卷资源
class QuestionnaireResource(Resource):

    @customer_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        state = data.get('state', False)
        limit = abs(int(data.get('limit', 15)))
        start_id = data.get('start_id', False)
        title = data.get('title', False)
        create_time = data.get('create_time', False)

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

        if create_time:
            create_time = datetime.strptime(create_time, '%Y-%m-%d')
            Qs.append(Q(datetime__gt=create_time))

        Qs.append(Q(customer=request.user.customer))

        if limit > 50:
            limit = 50

        objs = Questionnaire.objects.filter(*Qs)[:limit]

        data = []
        for obj in objs:
            # 构建单个问卷信息
            obj_dict = dict()
            obj_dict['id'] = obj.id
            obj_dict['title'] = obj.title
            obj_dict['logo'] = obj.logo
            obj_dict['datetime'] = datetime.strftime(obj.datetime, "%Y-%m-%d")
            obj_dict['deadline'] = datetime.strftime(obj.deadline, "%Y-%m-%d")
            obj_dict['catogory'] = obj.catogory
            obj_dict['state'] = obj.state
            obj_dict['quantity'] = obj.quantity
            obj_dict['background'] = obj.background
            # 读取全部标签
            obj_dict['marks'] = [{'id': mark.id, 'name': mark.name,
                                  'description': mark.description}for mark in obj.marks.all()]

            # 构建问卷下的问题
            obj_dict['questions'] = []
            for question in obj.question_set.all():
                # 构建单个问题
                question_dict = dict()
                question_dict['id'] = question.id
                question_dict['title'] = question.title
                question_dict['is_checkbox'] = question.is_checkbox
                # 构建问题选项
                question_dict['items'] = [{
                    "id": item.id,
                    "content": item.content
                } for item in question.questionitem_set.all()]
                # 将问题添加到问卷的问题列表中
                obj_dict['questions'].append(question_dict)
            # 将问卷添加到问卷列表中
            data.append(obj_dict)

        return json_response(data)

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
        questionnaire.logo = data.get('logo', '')
        # 特殊处理 创建时间使用当前时间
        questionnaire.datetime = datetime.now()
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
        questionnaire.catogory = data.get('catogory', '')
        # 特殊处理 问卷创建时,状态为草稿
        questionnaire.state = 0
        # 特殊处理 默认问卷数量为1份
        questionnaire.quantity = int(data.get('quantity', 1))
        questionnaire.free_count = int(data.get('quantity', 1))
        questionnaire.background = data.get('background', '')
        questionnaire.save()

        # 特殊处理 问卷的标签
        # 获取需要添加到问卷中的标签id列表
        mark_ids = data.get('mark_ids', [])
        # 根据id列表找出标签
        marks = Mark.objects.filter(id__in=mark_ids)
        # 把找出来的标签添加进问卷中
        questionnaire.marks.set(marks)
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
                id=questionnaire_id, customer=request.user.customer, state__in=[0, 1, 2, 3])
        except Exception as e:
            return params_error({
                'questionnaire_id': "找不到对应的问卷,或者问卷不可修改"
            })
        questionnaire.title = data.get('title', '标题')
        questionnaire.logo = data.get('logo', '')
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
        questionnaire.catogory = data.get('catogory', '')
        # 特殊state
        questionnaire.state = state

        questionnaire.quantity = int(data.get('quantity', 1))
        questionnaire.free_count = int(data.get('quantity', 1))
        questionnaire.background = data.get('background', '')
        questionnaire.save()
        # 特殊处理 问卷的标签
        # 获取需要添加到问卷中的标签id列表
        mark_ids = data.get('mark_ids', [])
        # 根据id列表找出标签
        marks = Mark.objects.filter(id__in=mark_ids)
        # 把找出来的标签添加进问卷中
        questionnaire.marks.set(marks)
        questionnaire.save()

        return json_response({
            "questionnaire": '更新成功'
        })

    @customer_required
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        ids = data.get('ids', [])
        objs = Questionnaire.objects.filter(
            id__in=ids, customer=request.user.customer, state__in=[0, 1, 2, 3])
        deleted_ids = [obj.id for obj in objs]
        objs.delete()
        return json_response({
            'deleted_ids': deleted_ids
        })


class QuestionResource(Resource):
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
        question.is_checkbox = data.get('is_checkbox', False)
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
            question_item.content = item
            question_item.save()

        return json_response({
            'id': question.id
        })

    @atomic
    @customer_required
    def post(self, request, *args, **kwargs):
        data = request.POST
        question_id = data.get('question_id', 0)
        # 判断需要修改的问题是否存在
        question_exits = Question.objects.filter(id=question_id, questionnaire__state__in=[
            0, 1, 2, 3], questionnaire__customer=request.user.customer)
        if not question_exits:
            return params_error({
                'question_id': "该问题找不到,或者该问题所在问卷无法修改"
            })
        # 更新问题的属性
        question = question_exits[0]
        question.title = data.get('title', '题纲')
        question.is_checkbox = data.get('is_checkbox', False)
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
            question_item.content = item
            question_item.save()

        return json_response({
            'question': '更新成功'
        })

    @atomic
    @customer_required
    def delete(self, request, *args, **kwargs):
        data = request.DELETE
        ids = data.get('ids', [])
        objs = Question.objects.filter(id__in=ids, questionnaire__state__in=[
            0, 1, 2, 3], questionnaire__customer=request.user.customer)

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


class QuestionnaireCommentResource(Resource):
    @atomic
    @superuser_required
    def put(self, request, *arg, **kwargs):
        data = request.PUT
        questionnaire_id = data.get('questionnaire_id')
        questionnaire_exits = Questionnaire.objects.filter(
            id=questionnaire_id, state=1)
        if not questionnaire_exits:
            return params_error({
                'questionnaire_id': '该问卷找不到,或者不可审核'
            })
        questionnaire = questionnaire_exits[0]
        is_agree = data.get('is_agree', False)
        comment = data.get('comment', '')
        if is_agree:
            questionnaire.state = 3
            questionnaire.save()
            return json_response({
                'comment': '审核通过'
            })
        if comment:
            questionnaire.state = 2
            questionnaire.save()
            questionnaire_comment = QuestionnaireComment()
            questionnaire_comment.datetime = datetime.now()
            questionnaire_comment.comment = comment
            questionnaire_comment.questionnaire = questionnaire
            questionnaire_comment.save()
            return json_response({
                'comment': '提交审核内容成功'
            })
        return params_error({
            'comment': '没有提供审核信息'
        })

    @customer_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        questionnaire_id = data.get('questionnaire_id', 0)
        questionnaire_exits = Questionnaire.objects.filter(
            id=questionnaire_id, customer=request.user.customer)
        if not questionnaire_exits:
            return params_error({
                'questionnaire_id': '该问卷不存在'
            })
        questionnaire = questionnaire_exits[0]
        comments = [{
            'id': item.id,
            'datetime': datetime.strftime(item.datetime, '%Y-%m-%d'),
            'comment': item.comment
        } for item in questionnaire.questionnairecomment_set.all()]

        return json_response(comments)


class QuestionnaireStateResource(Resource):
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


class AnswerResource(Resource):
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
        answer.datetime = datetime.now()
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
        objs.delete()
        return json_response({
            'deleted_ids': deleted_ids
        })

    @userinfo_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        limit = abs(int(data.get('limit', 30)))
        start_id = data.get('start_id', 0)
        is_done = data.get('is_done', False)
        objs = Answer.objects.filter(
            id__gt=start_id, userinfo=request.user.userinfo, is_done=is_done)

        data = []
        for obj in objs:
            answer_dict = dict()
            answer_dict['id'] = obj.id
            answer_dict['datetime'] = datetime.strftime(
                obj.datetime, '%Y-%m-%d')
            answer_dict['is_done'] = obj.is_done
            answer_dict['questionnaire'] = {
                'id': obj.questionnaire.id,
                'title': obj.questionnaire.title
            }
            data.append(answer_dict)

        return json_response(data)


class AnswerItemResource(Resource):

    def _save_answers(self, data, request):
         # 判断问卷是否存在
        questionnaire_id = data.get('questionnaire_id', 0)
        questionnaire_exist = Questionnaire.objects.filter(
            id=questionnaire_id, state=4, deadline__gt=timezone.now())
        if not questionnaire_exist:
            return params_error({
                "questionnaire_id": "问卷不存在,或者不可提交答案"
            })
        # 验证问卷是否可以提交答案
        questionnaire = questionnaire_exist[0]
        has_joined = Answer.objects.filter(
            questionnaire=questionnaire, userinfo=request.user.userinfo, is_done=False)
        if not has_joined:
            return params_error({
                'questionnaire_id': "还没有参与该问卷,或者该问卷已经完成"
            })

        questions = data.get('questions', [])

        # 可以提交答案的问题
        question_ids = [item['question_id'] for item in questions]
        questions_can_answer = Question.objects.filter(
            id__in=question_ids, questionnaire=questionnaire)
        questions_can_answer_ids = [obj.id for obj in questions_can_answer]
        # 如果有回答过该问题,那么清空该问题答案
        AnswerItem.objects.filter(
            question__in=questions_can_answer, userinfo=request.user.userinfo).delete()

        # data=[
        #   {
        #       "question_id":id,
        #       "items":[1,2,3]
        #   }
        # ]

        # 将用户的选项保存下来
        for question in questions:
            # 判断提交的问题是否合法
            if question['question_id'] in questions_can_answer_ids:
                question_obj = Question.objects.get(id=question['question_id'])
                answer = AnswerItem()
                answer.question = question_obj
                answer.userinfo = request.user.userinfo
                # 把该问题下选项找出来
                items = QuestionItem.objects.filter(
                    id__in=question['items'], question=question_obj)
                if items.count() > 1 and question_obj.is_checkbox:
                    answer.save()
                    answer.items.set(items)
                elif items.count() == 1:
                    answer.save()
                    answer.items.set(items)
                else:
                    return json_response({
                        "warnning": '参数错误'
                    })

        # 用户保存,或者提交答案
        answer = has_joined[0]
        is_done = data.get('is_done', False)
        answer.is_done = is_done
        answer.save()

        return json_response({'answer': "提交成功"})

    @atomic
    @userinfo_required
    def put(self, request, *args, **kwargs):
        data = request.PUT
        response = self._save_answers(data, request)
        return response

    @atomic
    @userinfo_required
    def post(self, request, *args, **kwargs):
        data = request.POST
        response = self._save_answers(data, request)
        return response

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
        answers = AnswerItem.objects.filter(
            userinfo=request.user.userinfo, question__questionnaire=questionnaire)
        data = [
            {
                "question_id": answer.question.id,
                "items": [{'id': item.id} for item in answer.items.all()]
            } for answer in answers
        ]

        return json_response(data)

# 审核管理员


class CommentQuestionnaire(Resource):
    @superuser_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        # 是否需要把详细信息返回去
        with_detail = data.get('with_detail', False)
        # 每页显示的数量
        limit = abs(int(data.get('limit', 10)))
        # 其实id
        start_id = abs(int(data.get('start_id', 0)))
        # 访问第几页
        page = abs(int(data.get('page', 1)))
        # 搜索所有待复核的问卷
        all_objs = Questionnaire.objects.filter(state=1, id__gt=start_id)
        # 获取所有待复核问卷数量
        count = all_objs.count()
        # 计算出总页数
        pages = math.ceil(count/limit)
        # 判断需要访问的页号
        if page >= pages:
            page = pages
        if page == 0:
            page = 1
        # 取出对应的页面
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]
        # 构建返回数据
        data = []
        for obj in objs:
            # 构建单个问卷信息
            obj_dict = dict()
            obj_dict['id'] = obj.id
            obj_dict['title'] = obj.title
            obj_dict['logo'] = obj.logo
            obj_dict['datetime'] = datetime.strftime(obj.datetime, "%Y-%m-%d")
            obj_dict['deadline'] = datetime.strftime(obj.deadline, "%Y-%m-%d")
            obj_dict['catogory'] = obj.catogory
            obj_dict['state'] = obj.state
            obj_dict['quantity'] = obj.quantity
            obj_dict['background'] = obj.background
            # 读取全部标签
            obj_dict['marks'] = [{'id': mark.id, 'name': mark.name,
                                  'description': mark.description}for mark in obj.marks.all()]
            # 是否构建详细信息
            if with_detail:
                # 构建问卷下的问题
                obj_dict['questions'] = []
                for question in obj.question_set.all():
                    # 构建单个问题
                    question_dict = dict()
                    question_dict['id'] = question.id
                    question_dict['title'] = question.title
                    question_dict['is_checkbox'] = question.is_checkbox
                    # 构建问题选项
                    question_dict['items'] = [{
                        "id": item.id,
                        "content": item.content
                    } for item in question.questionitem_set.all()]
                    # 将问题添加到问卷的问题列表中
                    obj_dict['questions'].append(question_dict)
            # 将问卷添加到问卷列表中
            data.append(obj_dict)

        return json_response(data)


class HomeQuestionnaireResource(Resource):
    @userinfo_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        # 是否需要把详细信息返回去
        with_detail = data.get('with_detail', False)
        # 每页显示的数量
        limit = abs(int(data.get('limit', 10)))
        # 其实id
        start_id = abs(int(data.get('start_id', 0)))
        # 访问第几页
        page = abs(int(data.get('page', 1)))
        has_joined = Answer.objects.filter(userinfo=request.user.userinfo)
        has_joined_questionnaire_ids = [item.questionnaire.id for item in has_joined]
        # 搜索所有可参与的问卷
        all_objs = Questionnaire.objects.filter(
            id__gt=start_id, state=4, deadline__gt=timezone.now(), free_count__gt=0).exclude(id__in=has_joined_questionnaire_ids)
        # 获取所有可参与问卷数量
        count = all_objs.count()
        # 计算出总页数
        pages = math.ceil(count/limit)
        # 判断需要访问的页号
        if page >= pages:
            page = pages
        if page == 0:
            page = 1
        # 取出对应的页面
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]
        # 构建响应数据
        data = []
        for obj in objs:
            # 构建单个问卷信息
            obj_dict = dict()
            obj_dict['id'] = obj.id
            obj_dict['title'] = obj.title
            obj_dict['logo'] = obj.logo
            obj_dict['datetime'] = datetime.strftime(obj.datetime, "%Y-%m-%d")
            obj_dict['deadline'] = datetime.strftime(obj.deadline, "%Y-%m-%d")
            obj_dict['catogory'] = obj.catogory
            obj_dict['state'] = obj.state
            obj_dict['quantity'] = obj.quantity
            obj_dict['background'] = obj.background
            obj_dict['customer'] = obj.customer.company
            # 读取全部标签
            obj_dict['marks'] = [{'id': mark.id, 'name': mark.name,
                                  'description': mark.description}for mark in obj.marks.all()]
            # 是否构建详细信息
            if with_detail:
                # 构建问卷下的问题
                obj_dict['questions'] = []
                for question in obj.question_set.all():
                    # 构建单个问题
                    question_dict = dict()
                    question_dict['id'] = question.id
                    question_dict['title'] = question.title
                    question_dict['is_checkbox'] = question.is_checkbox
                    # 构建问题选项
                    question_dict['items'] = [{
                        "id": item.id,
                        "content": item.content
                    } for item in question.questionitem_set.all()]
                    # 将问题添加到问卷的问题列表中
                    obj_dict['questions'].append(question_dict)
            # 将问卷添加到问卷列表中
            data.append(obj_dict)

        return json_response(data)


class UserQuestionnaireResource(Resource):
    @userinfo_required
    def get(self, request, *args, **kwargs):
        data = request.GET
        # 是否需要把详细信息返回去
        with_detail = data.get('with_detail', False)
        # 每页显示的数量
        limit = abs(int(data.get('limit', 10)))
        # 其实id
        start_id = abs(int(data.get('start_id', 0)))
        # 访问第几页
        page = abs(int(data.get('page', 1)))

        # 是否已完成
        is_done = data.get('is_done', False)
        if is_done == 'true':
            is_done = True
        else:
            is_done = False

        # 搜索所有可参与的问卷
        all_objs = Answer.objects.filter(
            userinfo=request.user.userinfo, is_done=is_done)
        # 获取所有可参与问卷数量
        count = all_objs.count()
        # 计算出总页数
        pages = math.ceil(count/limit)
        # 判断需要访问的页号
        if page >= pages:
            page = pages
        if page == 0:
            page = 1
        # 取出对应的页面
        start = (page-1)*limit
        end = page*limit
        objs = all_objs[start:end]
        # 构建响应数据
        questionnaires = [obj.questionnaire for obj in objs]
        data = []
        for obj in questionnaires:
            # 构建单个问卷信息
            obj_dict = dict()
            obj_dict['id'] = obj.id
            obj_dict['title'] = obj.title
            obj_dict['logo'] = obj.logo
            obj_dict['datetime'] = datetime.strftime(obj.datetime, "%Y-%m-%d")
            obj_dict['deadline'] = datetime.strftime(obj.deadline, "%Y-%m-%d")
            obj_dict['catogory'] = obj.catogory
            obj_dict['state'] = obj.state
            obj_dict['quantity'] = obj.quantity
            obj_dict['background'] = obj.background
            obj_dict['customer'] = obj.customer.company
            # 读取全部标签
            obj_dict['marks'] = [{'id': mark.id, 'name': mark.name,
                                  'description': mark.description}for mark in obj.marks.all()]
            # 是否构建详细信息
            if with_detail:
                # 构建问卷下的问题
                obj_dict['questions'] = []
                for question in obj.question_set.all():
                    # 构建单个问题
                    question_dict = dict()
                    question_dict['id'] = question.id
                    question_dict['title'] = question.title
                    question_dict['is_checkbox'] = question.is_checkbox
                    # 构建问题选项
                    question_dict['items'] = [{
                        "id": item.id,
                        "content": item.content
                    } for item in question.questionitem_set.all()]
                    # 将问题添加到问卷的问题列表中
                    obj_dict['questions'].append(question_dict)
            # 将问卷添加到问卷列表中
            data.append(obj_dict)

        return json_response(data)


# class InfoQuestionnaireResource(Resource):
#     def get(self, request, *args, **kwargs):
#         data = request.GET
#         start_id = int(data.get('start_id', 0))
#         with_detail = data.get('with_detail', False)
#         state = data.get('state', 3)
#         limit = int(data.get('limit', 10))
#         page = data.get('page', 1)
#         all_objs = Questionnaire.objects.filter(state=state, id__gt=start_id)
#         count = all_objs.count()
#         pages = math.ceil(count/limit)
#         if page >= pages:
#             page = pages
#         if page <= 1:
#             page = 1
#         start = (page-1)*limit
#         end = page*limit
#         objs = all_objs[start:end]
#         data = []
#         for obj in objs:
#             # 构建单个问卷信息
#             obj_dict = dict()
#             obj_dict['id'] = obj.id
#             obj_dict['title'] = obj.title
#             obj_dict['logo'] = obj.logo
#             obj_dict['datetime'] = datetime.strftime(obj.datetime, "%Y-%m-%d")
#             obj_dict['deadline'] = datetime.strftime(obj.deadline, "%Y-%m-%d")
#             obj_dict['catogory'] = obj.catogory
#             obj_dict['state'] = obj.state
#             obj_dict['quantity'] = obj.quantity
#             obj_dict['background'] = obj.background
#             # 读取全部标签
#             obj_dict['marks'] = [{'id': mark.id, 'name': mark.name,
#                                   'description': mark.description}for mark in obj.marks.all()]
#             if with_detail:
#                 # 找出客户信息
#                 obj_dict['customer'] = {
#                     'name': obj.customer.name,
#                     'email': obj.customer.email,
#                     'company': obj.customer.company,
#                     'address': obj.customer.address,
#                     'phone': obj.customer.phone,
#                     'mobile': obj.customer.mobile,
#                     'qq': obj.customer.qq,
#                     'wechat': obj.customer.wechat,
#                     'web': obj.customer.web,
#                     'industry': obj.customer.industry,
#                     'description': obj.customer.description,
#                 }
#                 # 构建问卷下的问题
#                 obj_dict['questions'] = []
#                 for question in obj.question_set.all():
#                     # 构建单个问题
#                     question_dict = dict()
#                     question_dict['id'] = question.id
#                     question_dict['title'] = question.title
#                     question_dict['is_checkbox'] = question.is_checkbox
#                     # 构建问题选项
#                     question_dict['items'] = [{
#                         "id": item.id,
#                         "content": item.content
#                     } for item in question.questionitem_set.all()]
#                     # 将问题添加到问卷的问题列表中
#                     obj_dict['questions'].append(question_dict)

#             # 将问卷添加到问卷列表中
#             data.append(obj_dict)

#         return json_response(data)
