from django_redis import get_redis_connection


def json_msg(code,msg=None,data=None):
    '''
        封装json消息
    '''
    return {'code':code,'errmsg':msg,'data':data}


def get_cart_count(request):
    '''获取 当前用户购物车总数量'''
    user_id = request.session.get("ID")
    if user_id is None:
        return 0
    else :
        r = get_redis_connection()
        #准备建
        cart_key =f'cart_{user_id}'
        #获取值
        values = r.hvals(cart_key)
        #准备一个总数量
        total_count = 0
        for v in values:
            total_count += int(v)

        return  total_count

