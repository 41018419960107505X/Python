from django.db import models

# Create your models here.
class Grades(models.Model):
	"""docstring for Grade"""
	gname = models.CharField(max_length=20)
	gdate = models.IntegerField()
	ggirlnum = models.IntegerField()
	gboynum  = models.IntegerField()
	idDelete = models.BooleanField(default=False)
	#重写__str__()方法
	def __str__(self):
		return "%s--%d--%d"%(self.gname,self.ggirlnum,self.gboynum)
	class Meta:
		db_table = ['grades']
		ording   = ['gname']


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)
class Students(models.Model):
	"""docstring for ClassName"""
	#定义一个类方法创建对象
	@classmethod
	def createStudent(cls , name , gender , age , contend , grade , isD=False):
		stu = cls(sname=name , sgender=gender , sage=age , scontend=contend , sgrade=grade , isDelete=isD)
		return stu
	  # 自定义管理器
    object1 = models.Manager()
    objects2 = StudentManager()

	sname = models.CharField(max_length=20)
	sgender = models.BooleanField(default=True)
	sage  = models.IntegerField()
	scontend = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	#关联外键
	sgrade   = models.ForeignKey('Grades')
	def __str__(self):
		return self.sname
	class Meta:
		db_table=['students']
		ording  =['id']#表示用id字段进行排序,此排序为升序
	
		