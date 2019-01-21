from django.conf.urls import url

from user.views import LoginView, RegisterView

urlpatterns = [
    # url(r'^login/$',LoginView.as_view(),name="登陆"),
    url(r'^login/$', LoginView.as_view(), name="login"),  # 用户登录
    url(r'^reg/$', RegisterView.as_view(), name="register"),  # 用户注册
    #url(r'^member/$', member, name="member"),  # 用户中心
    # url(r'^detail/(?P<id>\d+)/$',detail,name="详情"),
    # url(r'^add/$',add,name="添加"),
    # url(r'^delete/(?P<id>\d+)/$',delete,name="删除"),
    # url(r'^edit/(?P<id>\d+)/$',edit,name="修改"),
    # url(r'^add_form/$',add_form,name="渲染form"),
]