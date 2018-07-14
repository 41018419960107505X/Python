# 请求地址
url = 'https://api.miaodiyun.com/20150822/industrySMS/sendSMS'

# 请求头
headers = {'Content-type': 'application/x-www-form-urlencoded'}

# 账户sid
accountSid = '6c3617eb596b4817b7121d176da4beb1'

# auth token
auth_token = '1064346300b04feda39a88276e3b0c81'

# 时间戳
import time
timestamp = time.strftime('%Y%m%d%H%M%S')

sig = accountSid + auth_token + timestamp
# md5加密一下
import hashlib
md = hashlib.md5()
md.update(sig.encode('utf-8'))

sig = md.hexdigest()

# 模板参数
yzm = '632881'
t = '5'
param = yzm + ',' + t

# 表单数据
form_data = {
    'accountSid': accountSid,
    'templateid': '192310431',
    'to': '13523135987',
    'timestamp': timestamp,
    'sig': sig,
    'param': param,
}

# 将字典转换为url参数形式
from urllib.parse import urlencode
form_data = urlencode(form_data)

# 创建浏览器对象
import http.client
connect = http.client.HTTPConnection('api.miaodiyun.com')

# 发送POST请求
connect.request(method='POST', url=url, body=form_data, headers=headers)

# 获取响应
resp = connect.getresponse()

# 打印响应结果
print(resp.read().decode('utf-8'))
