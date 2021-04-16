from django.urls import path,re_path
from . import views,views1,views2

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
    path('index/', views2.index, name='index'),

    # 通用视图
    # as_view 源码中的dispatch函数将用户请求method映射成对应的function
    path('index/', views2.IndexView.as_view()),
]