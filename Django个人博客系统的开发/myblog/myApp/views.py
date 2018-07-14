from django.shortcuts import render

# Create your views here.
from django import HttpResponse
def index(request):
	return HttpResponse("sunck is a good man")


from .models import Grades , Students
def grades(request):
	#去模版里面取数据
	gradesList = Grades.objects1.all()
	#将数据传递给模板,模版在渲染页面,将渲染好的页面传递给浏览器
	return render(request,'myApp/grades.html',{'grades':gradesList})

def students(request):
	studentsList = Students.objects1.all()
	return render(request,'myApp/students.html',{'students':studentsList})

def gradeStudents(request,num):
	#获取对应的班级对象
	grade = Grades.objects1.get(pk=num)
	#获取班级下的所有学生列表
	studentsList = grade.students_set.all()
	return render(request,'myApp/students.html',{'students':studentsList})


from .models import Grades , Students
def addstudents(request):
	grade = Grades.objects2.get(pk=1)
	stu   = Students.Create('liudehua',True,25,'明天会更好',grade)
	stu.save()
	return HttpResponse('已经添加一位学生基本信息到数据库成功!!!')

#显示前5个学生
#分页显示学生
def pagestudent(request)
	studentsList = Students.objects2.all().[0:5]
	return render(request,'myApp/students.html',{'students':studentsList})

#分页显示学生
def pagestudent(request,page):
	page = int(page)
	studentsList = Students.objects2.all().[(page-1)*5:page*5]
	return render(request,'myApp/students.html',{'students':studentsList})



from django.http import HttpResponseRedirect , JsonResponse
from django.shortcuts import redirect
def redirect1(request):
		return redirect('/sunck/redirect2')
def redirect2(request):
	if request.is_ajax:
		#创建JsonResponse对象
		a = JsonResponse({})
		return HttpResponseRedirect('我是重定向过来的视图')

#状态保持
def main(request):
	#取session
	username = request.session.get('username','游客')
	return  render(request,'myApp/main.html',{'username':username})
def login(request):
	return render(request,'myApp/login.html')
def showmain(request):
	print('aaaaaaaaaaaaaaaaaaa')
	username = request.POST.get('username')
	#存储session值到数据库
	request.session['username']=username
	# 设置过期时间
	request.session.set_expiry(10)
	return redirect('/sunck/main/')
from django.contrib.auth  import logout
def quit(request):
	#清除session
	logout(request)
	#request.session.flush()
	return redirect('/sunck/main')


def index(request):
	return render(request,'myApp/index.html',{'code':'<h1>sunck is a good man</h1>'})







