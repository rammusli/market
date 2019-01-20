from django.shortcuts import render,HttpResponse

# Create your views here.
def user(request):
    html = "user "
    return HttpResponse(html)