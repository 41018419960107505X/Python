"""
# 通用接口
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
                data['category'] = 'userinfo'
                data['age'] = userinfo.age
                data['name'] = userinfo.name
                data['gender'] = userinfo.gender
                data['phone'] = userinfo.phone
                data['email'] = userinfo.email
                data['address'] = userinfo.address
                if userinfo.birthday:
                    data['birthday'] = userinfo.birthday.strftime("%Y-%m-%d")
                else:
                    data['birthday'] = datetime.now().strftime("%Y-%m-%d")
                data['qq'] = userinfo.qq
                data['wechat'] = userinfo.wechat
                data['job'] = userinfo.job
                data['salary'] = userinfo.salary
                # 用json把data转化成字符串,返回给客户端
            # 判断是否是客户
            elif hasattr(user, 'customer'):
                customer = user.customer
                # 构建json字典
                data = dict()
                data['user'] = user.id
                data['category'] = 'customer'
                data['name'] = customer.name
                data['email'] = customer.email
                data['company'] = customer.company
                data['address'] = customer.address
                data['phone'] = customer.phone
                data['mobile'] = customer.mobile
                data['qq'] = customer.qq
                data['wechat'] = customer.wechat
                data['web'] = customer.web
                data['industry'] = customer.industry
                data['description'] = customer.description
                # 用json把data转化称字符串,返回给客户端
            elif user.is_superuser:
                data = dict()
                data['user'] = user.id
                data['category'] = 'superuser'
            else:
                # 没有相关用户信息,返回空
                data = {}
            return json_response(data)

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
        # 开启数据库事务
        with atomic():
            user = User()
            user.username = username
            # 设置密码
            user.set_password(password)
            user.save()
            # 根据用户类型,创建普通用户或者客户
            if category == 'userinfo':
                UserInfo.create_userinfo(user=user, name='姓名')
            else:
                Customer.create_customer(user=user, name='名称')
            login(request, user)
            request.session['regist_code'] = False
            return json_response({
                "id": user.id
            })

    # 更新用户
    @atomic
    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        if user.is_authenticated:
            # 判断是否是普通用户
            if hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                userinfo.name = data.get('name', '姓名')
                userinfo.age = int(data.get('age', 0))
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


# 密码
class PasswordResource(Resource):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return not_authenticated()
        data = request.POST
        password = data.get('password', '')
        ensure_password = data.get('ensure_password', '')
        error = dict()
        if len(password) < 6:
            error['password'] = "密码长度不小于6位"
        if password != ensure_password:
            error['ensure_password'] = "密码不匹配"
        if error:
            return params_error(error)
        user = request.user
        user.set_password(password)
        user.save()
        login(request, user)
        return json_response({
            "msg": "密码更新成功"
        })


class QuestionnaireResource(Resource):
    def get(self, request, *args, **kwargs):
        return json_response({})
