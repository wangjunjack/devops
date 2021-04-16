from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView
from hello.models import User



def index(request):
    if request.method == 'GET':
        return HttpResponse('get')
    elif request.method == 'POST':
        return HttpResponse('post')
    elif request.method == 'PUT':
        return HttpResponse('put')
    elif request.method == 'DELETE':
        return HttpResponse('delete')

class IndexView(View):
    def get(self, request):
        return HttpResponse('get')

    def post(self, request):
        return HttpResponse('post')

    def put(self, request):
        return HttpResponse('put')

    def delete(self, request):
        return HttpResponse('delete')

#视图
class IndexView1(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'index.html', {'users':users})
    def post(self,request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, 'index.html', {'users':users})

# 视图模版
class IndexView2(TemplateView):
    template_name = 'index.html'  # 指定模版文件

    def get_context_data(self, **kwargs):
        # 将数据存入到context上下文中，给前端渲染
        contex = super(IndexView2, self).get_context_data(**kwargs)
        print(kwargs)
        contex['users'] = User.objects.all()
        print(contex)
        return contex

    def post(self, request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, 'index.html', {'users':users})

#listView 列表视图
from django.views.generic import ListView

class IndexView3(ListView):
    """
    listView适合以下场景
    getlist: 列出所有数据
    create：创建数据
    """
    # http://panfeng:8000/hell0/index3/
    template_name = 'index.html' # 指定模版文件
    model = User # object_list = User.objects.all(),做了这些操作，从数据库拿数据
    context_object_name = 'users' # 自定义传给前端模版的变量，默认object_list
    keyword = ''

    # http://panfeng:8000/hello/index3/?keyword=kk
    def get_queryset(self): # 过滤查询方法
        queryset = super(IndexView3, self).get_queryset()
        print(queryset)
        self.keyword = self.request.GET.get('keyword','')
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset

    def get_context_data(self, **kwargs):
        # 继承基础的ListView类
        context = super(IndexView3, self).get_context_data(**kwargs)
        print(context )
        # super()方法是继承父类
        # 在父类的基础上，再额外加一些数据到object_list中
        context['keyword'] = self.keyword
        print(context)
        return context
    # def post(self, request): # post请求
    #     data = request.POST.dict()
    #     print(data)
    #     User.objects.create(**data)
    #     users = User.objects.all()
    #     return render(request, 'index.html', {'users':users})


# DetailView
from django.views.generic import DetailView
from datetime import datetime, timezone
class IndexView4(DetailView):
    """
        获取某条记录的ID，适用于以下三种场景，核心就是拿到URL中的id
        getone: 获取当前记录数据
        update: 更新当前记录数据
        delete: 删除当前记录数据
    """
    # http://panfeng:8000/hello/index4/2
    template_name = 'index.html' # 指定模版文件
    model = User # object = User.objects.get(pk=pk)
    context_object_name = 'user' # 定义存储返回结果的对象名，默认object

    # 在 get_context_data() 函数中可以用于传递一些额外的内容到网页
    def get_context_data(self, **kwargs):
        # 返回某一条数据，**kwargs为where条件，即url中传入的PK 主键
        context = super(IndexView4, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        print(context)
        return context

# CreateView
from django.views.generic import CreateView,UpdateView,DeleteView
class IndexView5(CreateView):
    """
    添加用户
    """
    template_name = 'index.html'
    model = User
    fields = ('name', 'password', 'sex')

    def get_success_url(self): # 跳转方法
        return reverse('hello:index5')

    def get_context_data(self, **kwargs): # 页面数据填充
        context = super(IndexView5, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        print(context)
        return context

# UpdateView
class IndexView6(UpdateView):
    """
    更新用户
    """
    template_name = 'index.html'
    model = User
    fields = ('name', 'password', 'sex')

    def get_success_url(self): # 这个函数也是自行重写的方法，因为父类中已经有定义。
        # kwargs={'pk': self.kwargs['pk']} 获取pk方法
        print(self.kwargs) # 打印出pk参数
        return reverse('hello:index6', kwargs={'pk': self.kwargs['pk']}) # 跳转到自己到页面

    def get_context_data(self, **kwargs):
        context = super(IndexView6, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        print(context)
        return context

# DeleteView
class IndexView7(DeleteView):
    """
    删除用户
    """
    template_name = 'index.html'
    model = User

    def get_success_url(self): # 成功后的跳转，跳转到userlist
        return reverse('hello:userlist')

    def get_context_data(self, **kwargs):
        context = super(IndexView7, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        print(context)
        return context





