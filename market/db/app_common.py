from django.conf import settings
import hashlib

from django.http import JsonResponse
from django.shortcuts import redirect


# 加密  用 setting  中的   SECRET_KEY  加盐
from shoppingcart.helper import json_msg


def set_password(password):
    strs = '{}{}'.format(password, settings.SECRET_KEY)
    h = hashlib.md5(strs.encode('utf-8'))
    return h.hexdigest()


# 判断登录的装饰器
def judgeSignIn(fun):
    def new_fun(request, *args, **kwargs):
        if request.session.get('ID') is None:
            referer = request.META.get('HTTP_REFERER',None)
            if referer :
                request.session['referer'] = referer
            if request.is_ajax():
                return  JsonResponse(json_msg(1,'未登录'))
            else:
                return redirect('user:login')


        else:
            return fun(request, *args, **kwargs)
    return new_fun