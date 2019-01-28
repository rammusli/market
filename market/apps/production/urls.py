from django.conf.urls import url

from apps.production.views import IndexView, CategoryView, DetailView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),  # 商品首页
    url(r'^category/(?P<cate_id>\d+)/(?P<order>\d)/$', CategoryView.as_view(), name='category'),  # 商品分类（商品列表）
    url(r'^(?P<id>\d+).html$', DetailView.as_view(), name='detail'),  # 商品详情
]
