#导入配置文件
import os
import config
import tornado.web
from views import index
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
        	#(r'/',index.IndexHandler),
            (r'/',index.IndexHandler),
            (r'/home',index.HomeHandler),
            #StaticFileHandler,要放在所有路由的最下面
            (r'/(.*)$', tornado.web.StaticFileHandler,{"path":os.path.join(config.BASE_DIRS,"static/html"),"default_filename":"index.html"}),
            #反向解析
            tornado.web.url(r'/asdsdhsdh',index.KaigeHandler,{"word4":"man","word5":"hand"},name="index"),
        ]
        super(Application,self).__init__(handlers,**config.settings)


