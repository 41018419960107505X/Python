import tornado.web
from .sunckMysql import SunckMySQL
class ORM(tornado.web.RequestHandler):
    def save(self):
       #insert into students (name , age)  values('tyui',32)
        tableName = (self.__class__.__name__).lower()
        fieldsStr = valuesStr = "("
        for field in self.__dict__:
            fieldsStr += (field + ",")
            if  isinstance(self.__dict__[field] , str):
                valuesStr += ("'" + self.__dict__[field] + "',")
            else:
                valuesStr += (str(self.__dict__[field]) + ",")
        fieldsStr = fieldsStr[:len(fieldsStr)-1] + ")"
        valuesStr = valuesStr[:len(valuesStr)-1] + ")"
        sql = "insert into" + tableName + " " + fieldsStr + "values" + valuesStr

        #print(sql)
        db = SunckMySQL()
        #db2 = SunckMySQL()
        db.insert(sql)

    def delete(self):
        pass
    def update(self):
        pass

    @classmethod
    def all(cls):
        #select * from students
        tableName = (cls,__name__).lower()
        sql = "select * from " + tableName
        db = SunckMySQL()
        print(sql)
        return db.get_all_obj(sql , tableName)

    @classmethod
    def fillter(cls):
        pass