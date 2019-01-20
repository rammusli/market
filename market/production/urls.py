from django.conf.urls import url

from production.views import production

urlpatterns = [
    url(r'^$',production,name="首页"),

]