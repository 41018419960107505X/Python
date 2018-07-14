import json

from django.http.multipartparser import MultiPartParser
from django.middleware.common import MiddlewareMixin
from Api.utils import params_error


class DataConvert(MiddlewareMixin):
    """
    # 数据类型转换
    > 因为django只能解析使用post方式上传的formdata
    > 不能够解析通过其他方法上传的json,xml,text格式数据,所以这里面,我们需要手动来解析上传的数据
    """

    def process_request(self, request):
        method = request.method
        if 'application/json' in request.content_type:
            # 把客户端上传的json数据转化成python字典
            try:
                data = json.loads(request.body.decode())
                files = None
            except Exception as e:
                return params_error({
                    'body': '请求数据类型不正确'
                })
        elif 'multipart/form-data' in request.content_type:
            # 把客户端已formdata上传的数据进行解析,通常客户端会把上传的文件也放在formdata中,
            # 所以下面的解析会把上传的文件也解析出来
            data, files = MultiPartParser(
                request.META, request, request.upload_handlers).parse()
        else:
            data = request.GET
            files = None

        if 'HTTP_X_METHOD' in request.META:
            method = request.META['HTTP_X_METHOD'].upper()
            setattr(request, 'method', method)

        if files:
            setattr(request, '{method}_FILES'.format(method=method), files)
        setattr(request, method, data)
