from django.shortcuts import render,HttpResponse

# Create your views here.
def order(request):
    return render(request,'order.html')