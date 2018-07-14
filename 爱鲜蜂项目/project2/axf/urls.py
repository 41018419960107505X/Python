from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'^home/$', views.home),

    url(r'market/(\w+)/(\w+)/(\w+)/$', views.market),
    url(r'^market1/(\w+)/$', views.market1),

    url(r'^changecart/(\d+)/$', views.changecart),
    # 修改是否选中商品
    url(r'^changecart1/$', views.changecart1),
    # 下单
    url(r'^Orders/$', views.Orders),

    url(r'^cart/$', views.cart),

    url(r'^mine/$', views.mine),
    url(r'^login/$', views.login),
    url(r'^quit/$', views.quit),

    url(r'^address/$', views.address),
    url(r'^showAddress/$', views.showAddress),

    # 接口
    # url(r'^SlideShows/$', views.SlideShows),
    # url(r'^MainDescriptions/$', views.MainDescriptions),
    # url(r'^Products/(\d+)$', views.Products),

]
