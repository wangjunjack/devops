from django.shortcuts import render
from django.http import HttpResponse,QueryDict
from hello.models import User



# def index(request):
#     return HttpResponse("<p>Hello Django</p>")

# 2. 普通url带参数 http://ip:8000/?year=2021&month=04
# def index(request):
#     # 设置默认值获取数据更优雅
#     year = request.GET.get("year", "2021")
#     month = request.GET.get("month", "6")
#     return HttpResponse("year is %s,month is %s"% (year, month))

# 3.url通过识别关键字参数(?<参数名>参数类型)
# http://ip:8000/hello/2021/04
# def index(request, **kwargs):
#     print(kwargs)
#     year = kwargs.get('year')
#     month = kwargs.get('month')
#     return HttpResponse("year is %s,month is %s" % (year, month))

# 另一种写法--函数参数位置无关，以关键字为准备，更灵活
# def index(request, month, year):
#     return HttpResponse("year is %s,month is %s" % (year,month))

################ POST 请求传参 ################
# def index(request):
#     print(request.scheme)
#     print(request.method)
#     print(request.headers)
#     print(request.path)
#     print(request.META)
#     print(request.GET)
#     data = request.GET
#     year = data.get("year", "2021")
#     month = data.get("month", "04")
#     if request.method == "POST":
#         print(request.method)
#         print(request.body)
#         print(QueryDict(request.body).dict())
#         print(request.POST)
#         data = request.POST
#         year = data.get("year", "2021")
#         month = data.get("month", "04")
#     return HttpResponse("year is %s,month is %s" % (year,month))

# template渲染数据到html
def index(request):
    classname = "devops"
    books = ['python', 'java', 'Django']
    user = {'name':'dev','age':'30'}
    userlist = [{'name':'dev','age':'30'}, {'name':'rock', 'age':'29'}, {'name':'mage', 'age':'10'}]
    return render(request, 'hello/hello.html', \
                  {'classname': classname, "books":books, "user":user, "userlist":userlist})
    # return render(request, 'hello/hello.html')

# list user
def list(request):
    messages = ['1', '2', '3', '4', '5']
    value = ['python', 'django', 'java'] # python,django,java前端想这样展示
    # users = [
    #         {'username': 'dev', 'name_cn': 'dev', 'age': 18},
    #         {'username': 'dev1', 'name_cn': 'dev1', 'age': 19},
    #         {'username': 'dev2', 'name_cn': 'dev2', 'age': 20},
    #     ]
    users = User.objects.all()
    print(users)
    return render(request, 'hello/userlist1.html', {'users':users, 'messages':messages, 'value':value})

# def userlist(request):
#     users = User.objects.all()
#     return render(request, 'index.html', {'users':users})
def user(request):
    return render(request, 'hello/userlist1.html')


