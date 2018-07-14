"""
# 客户接口
"""
import random
import json
import math
from datetime import datetime, timedelta

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
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


class PaymentBack(Resource):
    @atomic
    def get(self, request, *args, **kwargs):
        data = request.GET
        try:
            amount = int(data['amount'])
            flow = WalletFlow.objects.get(id=data['flow_id'])
            if amount <= 0:
                raise Exception('金额不合法')
        except Exception:
            return HttpResponse('参数错误')
        # 修改可用余额
        wallet = flow.wallet
        wallet.balance = wallet.balance+amount
        wallet.save()
        # 修改flow状态
        flow.done = True
        flow.save()
        return HttpResponseRedirect('/')

    def post(self, request, *args, **kwargs):
        data = request.POST
        try:
            amount = int(data['amount'])
            flow = WalletFlow.objects.get(id=data['flow_id'])
            if amount <= 0:
                raise Exception('金额不合法')
        except Exception:
            return HttpResponse('参数错误')
        # 修改可用余额
        wallet = flow.wallet
        wallet.balance = wallet.balance+amount
        wallet.save()
        # 修改flow状态
        flow.done = True
        flow.save()
        return HttpResponseRedirect('/')
