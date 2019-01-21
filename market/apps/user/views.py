from django.shortcuts import render, redirect
from django.http import  HttpResponse
from django.views import View
from user.forms import RegisterModelForm, LoginModelForm
from user.helper import set_password
from user.models import User
from django.urls import reverse


class LoginView(View):
    #get 请求获取登录页面
    def get(self,request):
        return  render(request,'user/login.html')
    #post 请求获取用户信息并验证
    def post(self,request):
        #获取数据
        data = request.POST
        #表单验证
        form = LoginModelForm(data)
        if form.is_valid():
            user = form.cleaned_data.get("user")
            request.session['id']=user.pk
            request.session['user_phone']=user.user_phone
            # request.session.set_expiry(0)
            return redirect(reverse("user:member"))
        else:
            # 数据不合法
            return render(request, 'user/login.html', context={"form": form})


#完成注册功能
class RegisterView(View):
    # get 方法
    def get(self, request):
        # 展示注册的页面
        return render(request, 'user/reg.html')

    # post 方法
    def post(self, request):
        # 接受用户提交的注册信息
        data = request.POST
        form = RegisterModelForm(data)
        if form.is_valid():
            # 数据合法
            cleaned_data = form.cleaned_data
            # 操作数据库, 创建一个用户
            user = User()
            user.user_phone = cleaned_data.get('user_phone')
            # 将密码进行加密
            user.user_password = set_password(cleaned_data.get('password2'))
            # 然后将用户信息保存到数据库
            user.save()
            # 跳转到登录界面
            return redirect(reverse('user:login'))

        else:
            # 不合法
            return render(request, 'user/reg.html', context={"form": form})

# def member(request):
#     return render(request,'user/member.html')