import random
import re
import uuid

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View

from db.app_common import set_password
from db.base_view import BaseVerifyView
from user.forms import RegisterModelForm, LoginModelForm
from django_redis import get_redis_connection

from user.helper import send_sms
from user.models import User
from django.urls import reverse


# 完成注册功能
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





#完成登陆功能
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




class PersonalCenter(BaseVerifyView):
    def get(self, request):
        tellphone = request.session.get("tellphone")
        context = {
            "tellphone": tellphone
        }
        return render(request, 'user/member.html')

    def post(self, request):

        return render(request, 'user/member.html')


#完成密码忘记功能
class Forget(View):

    def get(self, request):
        return render(request, "user/forgetpassword.html")

    def post(self, request):
        return redirect(reverse("user:login"))

#个人资料
class Info(BaseVerifyView):
    """
    用户个人资料
    """

    def get(self, request):
        tellphone = request.session.get("tellphone")
        user = User.objects.filter(user_telphone=tellphone).first()
        context = {
            "user": user
        }
        return render(request, "user/infor.html", context)

    def post(self, request):
        tellphone = request.session.get("tellphone")
        user = User.objects.get(user_telphone=tellphone)
        if request.FILES.get("user_head"):
            user.user_head = request.FILES.get("user_head")
            user.user_name = request.POST.get("nickname")
            user.user_gender = request.POST.get("gender")
            user.user_brith = request.POST.get("birth_of_date")
            user.user_school = request.POST.get("school")
            user.user_address = request.POST.get("address")
            user.user_hometown = request.POST.get("hometown")
            user.save()
        return redirect("user:info")

class SendMsg(View):
    """发生短信的视图函数"""
    def post(self,request):
        # 接收到手机号码
        user_phone = request.POST.get("user_phone", "")
        # 后端验证手机号码格式是否正确
        # 创建正则对象
        phone_re = re.compile("^1[3-9]\d{9}$")
        # 匹配传入的手机号码
        rs = re.search(phone_re, user_phone)
        if rs is None:
            # 手机号码格式错误
            return JsonResponse({"error": 1, "errmsg": "手机号码不正确"})
        # 生成随机码 随机数字组成
        random_code = "".join([str(random.randint(0, 9)) for _ in range(4)])

        # 保存随机码到redis中
        # 使用redis, 获取redis连接
        r = get_redis_connection("default")
        # 直接开始操作
        r.set(user_phone, random_code)
        # 设置过期时间
        r.expire(user_phone, 120)
        # 发送短信
        print(random_code)
        key_times ="{}_time".format(user_phone)
        now_times = r.get(key_times)
        if now_times is None or int(now_times) < 50:
            r.incr(key_times)
            #将信息保存1小时，5次请求之后就起到阻隔作用
            r.expire(key_times,3600)
        else:
            return JsonResponse({"error":1,"errmsg":"次数过多"})
        # 使用阿里发生短信

        __business_id = uuid.uuid1()
        params = "{\"code\":\"%s\",\"product\":\"天气不错\"}" % random_code
        print(send_sms(__business_id, user_phone, "注册验证", "SMS_2245271", params))

        return JsonResponse({"error": 0})


