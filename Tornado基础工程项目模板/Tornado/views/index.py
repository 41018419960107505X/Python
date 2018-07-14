import tornado.web
from tornado.web import RequestHandler
class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello word')

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('home')


class KaigeHandler(RequestHandler):
    def initialize(self , word4 , word5):
        self.word4 = word4
        self.word5 = word5
    def get(self, *args, **kwargs):
        print(self.word4 , self.word5)
        self.write("kaige is a good man")
















