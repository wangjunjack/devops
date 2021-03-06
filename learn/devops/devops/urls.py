"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.urls import path,include
from hello import views

# 用户输入是 http://ip:80081/hello
# 从hello app中定一个叫views.py模块index函数来处理hello这个用户请求
# from hello import views
app_name = 'hello'
urlpatterns = [
    # path('admin/', admin.site.urls),
    # 如果hello，总入口直接指向具体app等具体方法，一旦app过多，路由过多，注入口将不堪重负，所以要分而治之
    # path('hello/', views.index),
    # 当你访问hello时，我不知道具体方法，而是告诉你去hello app中的urls.py
    path('hello/', include('hello.urls')),
    # 关键字匹配(最优雅) (?<参数>参数类型) 视图中直接通过参数名获取值(最常用)
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index'),
]













