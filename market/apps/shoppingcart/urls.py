from django.conf.urls import url

from shoppingcart.views import AddCartView

urlpatterns = [
    url(r'^add/$',AddCartView.as_view(),name='addcart'),

]