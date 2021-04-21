from django import forms
from hello.models import User

# 原生表单验证各种表单类型及自定义
class UserForm(forms.Form):
    name = forms.CharField(max_length=10)
    phone = forms.CharField(max_length=10, required=False)
    email = forms.EmailField(max_length=10, required=False)
    password = forms.CharField(max_length=10, required=False)
    sex = forms.CharField(max_length=10, required=False)
    hobby = forms.CharField(max_length=10, required=False)
    skill = forms.CharField(max_length=10, required=False)
    file = forms.FileField()
    info = forms.CharField(max_length=100, required=True)

    # 自定义验证格式 clean_字段
    """
    Django的form系统自动寻找匹配的函数方法，该方法名称为clean_开头,并以字段名称结束。
    如果有这样的方法，它将在校验时被调用。clean_info()方法将在指定字段的默认校验逻辑执行之后被调用。
    本例中，在必填CharField这个校验逻辑之后，因为字段数据已经被部分处理，所以它被从self.cleaned_data
    中提取出来了。同样，我们不必担心数据是否为空，因为它已经被校验过了。
    """
    def clean_info(self):
        info = self.cleaned_data['info']
        print(info.split())
        num_info = len(info.split())
        if num_info < 4:
            raise forms.ValidationError("Info not enough words!")
        return info

# 原生表单渲染前端，简洁版本
class UsersForm(forms.Form):
    name = forms.CharField(max_length=10, required=True)
    password =  forms.CharField(max_length=12, required=True, widget=forms.PasswordInput)


class User1Form(forms.Form):
    """
        error_messages: 自定义报错信息，默认为系统自动提供的信息，如：此字段不能为空
        widget: 定义表单的样式
    """

    # 自定义下拉菜单的key/value
    JOB_STATUS = (
        (1, '在职'),
        (2, '离职'),
    )
    # id表单，隐藏不显示，并且定义了bootstrap的样式
    id =  forms.IntegerField(required=False,
                             widget=forms.HiddenInput(attrs={'class': 'form-control hidden'}))

    name = forms.CharField(required=True,
                           max_length=32,
                           error_messages={'required': '不能为空', 'max_length': '最多32字符'},
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(required=True,
                               max_length=32,
                               error_messages={'required': '不能为空', 'max_length': '最多32个字符'},
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone_num = forms.CharField(required=False,
                                max_length=11,
                                error_messages={'invalid': '手机格式错误'},
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))

    birthday = forms.DateField(required=True,
                               error_messages={'required': '生日不能为空'},
                               widget=forms.DateInput(attrs={'class': 'form-control datepicker-control'}))

    job_status = forms.IntegerField(required=True,
                                    error_messages={'required': '工作状态不能为空.'},
                                    widget=forms.Select(attrs={'class': 'select2'}, choices=JOB_STATUS))

    remark = forms.CharField(required=False,
                             max_length=255,
                             error_messages={'max_length': '最多255个字符'},
                             widget=forms.TextInput(attrs={'class': 'form-control'}))


# ModelForm
class UserModelForm(forms.ModelForm):
    pass













