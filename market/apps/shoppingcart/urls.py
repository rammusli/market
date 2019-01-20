from django.conf.urls import url

from shoppingcart.views import shoppingcart

urlpatterns = [
    url(r'^$',shoppingcart,name="首页"),

]