from django.conf.urls import url

from apps.production.views import IndexView, CategoryView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 商品首页
    url(r'^category/$', CategoryView.as_view(), name='category'),  # 商品分类（商品列表）
    url(r'^detail/$', DetailView.as_view(), name='detail'),  # 商品详情
]
