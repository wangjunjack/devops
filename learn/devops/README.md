## Django Learn
### Day1 MTV（Model Template Views）
1. 创建App
```shell
python manage.py startapp hello
```
2. 注册App到devops工程项目中

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hello.apps.HelloConfig',
]
```

3. 设计路由实现

需求：用户输入请求地址 http://ip:8000/hello 网页返回`Hello Django`

* 方案一
```python
# 主路由
from django.contrib import admin
from django.urls import path
from django.urls import path,include

# 用户输入是 http://ip:80081/hello
# 从hello app中定一个叫views.py模块index函数来处理hello这个用户请求
from hello import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # 如果hello，总入口直接指向具体app等具体方法，一旦app过多，路由过多，注入口将不堪重负，所以要分而治之
    path('hello/', views.index),
    # 当你访问hello时，我不知道具体方法，而是告诉你去hello app中的urls.py
    # path('', include('hello.urls')),
]

# 子路由

from django.urls import path
from . import views

urlpatterns = {
    path('hello/', views.index, name='index')
}
```

* 方案二
```python
# 主路由
from django.contrib import admin
from django.urls import path
from django.urls import path,include

# 用户输入是 http://ip:80081/hello
# 从hello app中定一个叫views.py模块index函数来处理hello这个用户请求
# from hello import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # 如果hello，总入口直接指向具体app等具体方法，一旦app过多，路由过多，注入口将不堪重负，所以要分而治之
    # path('hello/', views.index),
    # 当你访问hello时，我不知道具体方法，而是告诉你去hello app中的urls.py
    path('', include('hello.urls')),
]

# 子路由
from django.urls import path
from . import views

urlpatterns = {
    path('hello/', views.index, name='index')
}
```

