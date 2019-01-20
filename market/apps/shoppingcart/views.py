from django.shortcuts import render,HttpResponse

# Create your views here.
def shoppingcart(request):
    #html = "shoppingcart "
    return render(request, 'shopcart.html')