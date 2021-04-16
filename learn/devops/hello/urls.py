from django.urls import path,re_path
from . import views,views1,views2
from hello.views2 import IndexView,IndexView2

app_name = 'hello'
urlpatterns = [
    path('hello/', views.index, name='index'),
    path('list/', views.list, name = 'list'),

    # 简易用户管理系统
    path('useradd/', views1.useradd, name="useradd"),
    path('userlist/', views1.userlist, name="userlist"),
    re_path('modify/(?P<pk>[0-9]+)?/', views1.modify, name="modify"),
    re_path('userdel/(?P<pk>[0-9]+)?/', views1.userdel, name="userdel"),


    # FBV 实现增删改查
    # path('index/', views2.index, name='index'),

    # 通用视图
    # as_view 源码中的dispatch函数将用户请求method映射成对应的function
    path('index/', views2.IndexView.as_view()),

    # View
    path('index1/', views2.IndexView1.as_view()),
    # TemplateView
    path('index2/', views2.IndexView2.as_view(), name='index2'),
    re_path('index2/(?P<pk>[0-9]+)?/', views2.IndexView2.as_view(), name='index2'),

    # ListView--查询数据表所有数据
    path('index3/', views2.IndexView3.as_view(), name='index3'),

    # DetailView--查询数据表的某一条数据
    re_path('index4/(?P<pk>[0-9]+)?/', views2.IndexView4.as_view(), name='index4'),

    # CreateView--创建数据
    path('index5/',views2.IndexView5.as_view(), name='index5'),

    # UpdateView--更新数据
    re_path('index6/(?P<pk>[0-9]+)?/', views2.IndexView6.as_view(), name='index6'),

    # DeleteView--删除数据
    re_path('index7/(?P<pk>[0-9]+)?/', views2.IndexView7.as_view(), name='index7'),
    # (?P<pk>[0-9]+)? -> 这个是ID的写法，用户后端出入到前端的ID

]