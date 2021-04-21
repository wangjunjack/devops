from django.shortcuts import render,reverse
from django.views.generic import View,TemplateView,DetailView,ListView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse,HttpResponseRedirect
from hello.models import User

"""
form验证
"""
class UserAddView(SuccessMessageMixin, CreateView):
    """
    创建用户
    """
    model = User
    fields = ('name', 'password', 'sex')
    success_message = '%(name)s was created successfully'

    def get_success_url(self):
        if '_addanother' in self.request.POST:
            return reverse('hello:useradd1')
        return reverse('hello:list')

    def form_valid(self, form):
        """
        If the form is valid, redirect to the supplied URL.
        如果表单有效，则重定向到所提供的URL
        :param form:
        :return:
        """
        print(form)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the context data with the
        data-filled form and errors.
        如果表单无效，则重新呈现上下文数据，并填充表单和错误。
        :param form:
        :return:
        """
        print(form)
        print(form.errors)
        # print(form.name.errors)
        return self.render_to_response(self.get_context_data(form=form))

class UserDetailView(DetailView):
    """
    个人主页
    """
    template_name = "hello/user_detail.html"  #默认模版路径：hello/user_detail.html
    model = User                 # object = User.object.get(pk=pk)
    context_object_name = "user" # 自定义传给前端模版渲染的变量，默认boject

class UserListView(ListView):
    """
    用户列表
    """
    # template_name = "hello/user_list.html" # 默认模版路径：hello/user_list.html 可不写
    model = User                             # object_list = User.objects.all()
    context_object_name = "users"            # 自定义传给前端模版渲染的变量，默认object_list
    keyword = ""

    # 数据过滤
    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        self.keyword = self.request.GET.get("keyword", "")
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset

    # 需要传给前端的数据大字典
    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['keyword'] = self.keyword
        return context

class UserUpdateView(SuccessMessageMixin, UpdateView):
    """
    更新用户
    """
    # update 和create 默认的模版名都是hello/user_form.html ,为了方便看，我们重写一个
    # 这两共用一个form技术上是没问题的。生产环境中，create和update的字段可能并不完全一致
    template_name = 'hello/user_edit.html'
    model = "User"
    fields = ('name', 'password', 'sex')
    success_message = '%(name)s was update Successfully'

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse('hello:modify1', kwargs={'pk': self.object.pk})
        return reverse('hello:userlist1')


class UserDeleteView(DeleteView):
    """
    删除用户
    """
    # template_name = 'hello/user_confirm_delete.html'
    model = User

    def get_success_url(self):
        return reverse('hello:userlist1')


