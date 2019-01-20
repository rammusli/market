from django.shortcuts import render,HttpResponse

# Create your views here.
from django.views import  View

#登陆视图类，完成登陆功能
class LoginView(View):
    def get(self,request):
        return  render(request,'user/login.html')

    def post(self,request):
        pass


# def user(request):
#     #html = "user "
#     return render(request,'member.html')