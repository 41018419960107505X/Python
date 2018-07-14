import os
BASE_DIRS = os.path.dirname(__file__)
#参数
options = {
    "port":8000,
}

#数据库配置
mysql = {
    "host":"47.94.210.177",
    "user":"root",
    "passwd":"Sunck1999",
    "dbName":"AXF",
}
#配置
settings = {

    #配置静态文件路径
    "static_path":os.path.join(BASE_DIRS,"static"),
    #配置模板文件路径
    "template_path":os.path.join(BASE_DIRS,"templates"),
    #配置上传文件路径
    "upfile_path":os.path.join(BASE_DIRS,"upfile"),
    #"autoescape":None,
    "debug":False,
    "cookie_secret":"Vef2CLuAQwupGW0j+w397/AdNvb2+UsMmdvnKWTzrpk=",
    "xsrf_cookies":True,
    #用户验证(相当于重定向)
    "login_url":"/denglu"
}