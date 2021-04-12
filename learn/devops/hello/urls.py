from django.urls import path
from . import views

app_name = 'hello'
urlpatterns = {
    path('hello/', views.index, name='index'),
    path('list/', views.list, name='list'),
}