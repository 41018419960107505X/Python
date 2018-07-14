import os
import sys

from django.conf.urls import url

from Api.rest import *

# # 新建session对象
# session_obj = SessionRest()
# # 新建user对象
# user_obj= UserRest()

# api_urls = [
#     url(r'session', session_obj.enter),
#     url(r'user',user_obj.enter)
# ]

api=Register()
api.regist(SessionRest('session'))
api.regist(UserRest('user'))



