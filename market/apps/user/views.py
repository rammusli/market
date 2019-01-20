from django.shortcuts import render,HttpResponse

# Create your views here.

def user(request):
    #html = "user "
    return render(request,'member.html')