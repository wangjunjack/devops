from django.shortcuts import reverse,render
from django.views.generic import View,TemplateView

import  os
from hello.form import UserForm
from hello.form import UsersForm
from hello.form import User1Form


class HtmlView(TemplateView):
    template_name = 'test.html' # 指定模版文件

    def post(self, request):
        print(request.POST)

        # 一键一值的场景
        # data = request.POST.dict()
        # print(data)

        # 一键多值的场景 getlist
        # hobby = request.POST.getlist('hobby', '')
        # print(hobby)

        # 自定义一个高效的方法
        data1 = dict((k,','.join(v)) for k,v in dict(request.POST).items())
        # print(data1)

        # 接受文件，并以二进制的方式读取文件，然后存储
        # file = request.FILES.get('file', None)
        # print(file)
        # print(type(file))
        # if file:
        #     f = open(os.path.join('upload',file.name),'wb')
        #     for line in file.chunks():
        #         f.write(line)
        #     f.close()

        form = UserForm(request.POST, request.FILES)
        print("已经进行了表单验证")
        if form.is_valid():
            print("表单验证成功")
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            file = form.cleaned_data['file']
            print(file)
            if file:
                f = open(os.path.join('upload', file.name), 'wb')
                for line in file.chunks():
                    f.write()
                f.close()
        return render(request, 'test.html', {'form':form})
        # return render(request, 'test.html')

class FormView(View):
    def get(self, request):
        # form = UsersForm()                                  # 实例化一个表单对象，如果没有提交数据，就是显示空表单
        form = User1Form
        return render(request, 'form.html', {'form':form}) # 空表单在前台显示

    def post(self, request):
        # form = UsersForm(request.POST)                      # 将表单的数据绑定到form变量中
        form = User1Form(request.POST)
        if form.is_valid():                                 # 判断用户输入的数据类型是否合法
            print(form.cleaned_data)                        # 获取数据，数据就会保存在cleaned_data的字典中
            name = form.cleaned_data['name']                # 可以获取用户提交的信息
        return render(request, 'form.html', {'form':form})


class UserModelFormView(View):
    pass




















