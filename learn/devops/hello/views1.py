from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404,HttpResponse,QueryDict
from hello.models import User

import traceback

# 添加用户
def useradd(request):
    """
        添加用户
        request获取表单提交的数据有多种方式：
        1、request.POST.get---适用于获取单个变量进行处理的场景
        2、request.POST.dict()---适用于将表单所有数据整体处理的场景
        3、Form(request.POST)---适用于表单类验证的场景（生产中最常用）
    """
    msg = {}
    if request.method == "POST":
        try:
            print(request.POST)
            # 第一中方式一个个获取值，然后一个个入库
            # name = request.POST.get('name',"")
            # password = request.POST.get('password',"")
            # sex = request.POST.get('sex',"")
            # u = User()
            # u.name = name
            # u.password = password
            # u.sex = int(sex)
            # u.save()

            # 第二种方法，将提交的数据转换为字典，一次性入库
            data = request.POST.dict()
            print(data)
            User.objects.create(**data)
            msg = {"code": 0, "result": "添加用户成功"}
        except:
            msg = {"code": 1, "errmsg": "添加用户失败：%s"% traceback.format_exc()}
    return render(request, "hello/useradd.html", {"msg": msg})

# 用户列表
def userlist(request):
    """
    用户列表 && 姓名搜索
    :param request:
    :return:
    """
    keyword = request.GET.get("keyword","")
    users = User.objects.all()
    if keyword:
        users = users.filter(name__icontains=keyword)
    print(users)
    return render(request, 'hello/userlist.html', {"users":users, "keyword":keyword})

# 用户信息修改
def modify(request, **kwargs):
    """
    用户更新
    1、通过ID拿到要更新的数据，并传到前端渲染
    2、将修改后的数据提交到后端
    """
    msg = {}
    print(kwargs)
    pk = kwargs.get("pk")
    # user = User.objects.get(pk=pk) #不太严谨
    user = get_object_or_404(User, pk=pk)

    # 提交更新过的数据到数据库
    if request.method == "POST":
        try:
            data = request.POST.dict()
            print(data)
            User.objects.filter(pk=pk).update(**data)
            msg = {"code": 0, "result": "更新用户成功"}
        except:
            msg = {"code": 1, "errmsg": "更新用户失败: %s" % traceback.format_exc()}
    return render(request, "hello/modify.html", {"user":user, "msg":msg})

# 用户删除
def userdel(request, **kwargs):
    """
    用户删除
    :param request:
    :param kwargs:
    :return:
    """
    msg = {}
    pk = kwargs.get("pk")
    try:
        # 获取当前数据内容
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404
    if request.method == "POST":
        try:
            User.objects.get(pk=pk).delete()
            msg = {"code": 0, "result": "用户删除成功"}
        except:
            msg = {"code": 1, "errmsg": "删除用户失败: %s" % traceback.format_exc()}
    return render(request, "hello/userdel.html", {"user":user, "msg":msg})


