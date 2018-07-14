from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^grades/$',views.grades),
    url(r'^students/$',views.students),
    url(r'^grades/(\d+)',views.gradeStudents),
    url(r'^addstudents/$',views.addstudents),
    url(r'^redirect1/$',views.redirect1),
    url(r'^redirect2/$',views.redirect2),
    url(r'^main/$',views.main),
    url(r'^login/$',views.login),
    url(r'^showmain/$',views.showmain),
    url(r'^quit/$',views.quit),
    url(r'^/sunck/index/$',views.index),
    url(r'^upfile/$',views.upfile),
     url(r'^savefile/$',views.savefile),

    ]
