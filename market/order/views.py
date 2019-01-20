from django.shortcuts import render,HttpResponse

# Create your views here.
def order(request):
    html = "order "
    return HttpResponse(html)