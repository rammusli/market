from django.conf.urls import url

from order.views import order

urlpatterns = [
    url(r'^$',order,name="首页"),

]