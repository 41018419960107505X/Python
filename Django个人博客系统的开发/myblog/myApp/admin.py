from django.contrib import admin

# Register your models here.
from .models import Grades , Students
class StudentsInfo(admin.TabularInline):
	model = Students
	extra = 2
class GradesAdmin(admin.ModelAdmin):
		inlines = [StudentsInfo]
	#列表页属性

	#显示字段
	list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
	#过滤字段
	list_filter = ['gname']
	#搜索字段
	search_fields =['gname']
	#分页
	list_per_page = 5

	#添加修改页属性

	#规定属性的先后顺序
	fields = ['ggirlnum','gboynum','gname','gdate','isDelete']
	#给属性添加分组
	fieldsets = [('num',{'fields':['ggirlnum','gboynum']})
				 ('base',{'fields':['gname','gdate','isDelete']})
	]
	注意:fields与fieldsets不能同时使用

class StudentsAdmin(admin.ModelAdmin):
	def gender(self):
		if self.sgender:
			return "男"
		else:
			return "女"
		#设置页面列的名称
		gender.short_description = "性别"
	list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']
	actions_on_top = False
	actions_on_bottom True
#注册
admin.site.register(Grades ,GradesAdmin)
admin.site.register(Students,GradesAdmin)
