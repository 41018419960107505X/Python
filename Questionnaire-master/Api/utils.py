import json
import qrcode
from tempfile import TemporaryFile
import base64

from django.http.response import HttpResponse
import qrcode


def method_not_allowed():
    return HttpResponse(json.dumps({
        "state": 405,
        "msg": '方法不支持',
    }), content_type="application/json")


def json_response(data):
    json_data = {
        'state': 200,
        'msg': 'OK',
        'data': data
    }
    return HttpResponse(json.dumps(json_data), content_type='application/json')


def server_error():
    return HttpResponse(json.dumps({
        'state': 500,
        'msg': '服务器发生错误'
    }), content_type='application/json')


def not_found():
    return HttpResponse(json.dumps({
        'state': 404,
        'msg': '没有找到页面'
    }), content_type='application/json')


def params_error(data={}):
    return HttpResponse(json.dumps({
        'state': 422,
        'msg': '参数错误',
        'data': data
    }), content_type='application/json')


def not_authenticated():
    return HttpResponse(json.dumps({
        'state': 401,
        'msg': '未登录'
    }), content_type='application/json')


def permission_denied():
    return HttpResponse(json.dumps({
        'state': 403,
        'msg': '没有权限'
    }), content_type='application/json')


def create_qrcode(data):
    img = qrcode.make(data)
    tmp = TemporaryFile()
    img.save(tmp)
    tmp.seek(0)
    return base64.b64encode(tmp.read()).decode()
