from django.shortcuts import render,HttpResponse

# Create your views here.
def production(request):
    #html = "production "
    return render(request,'index.html')