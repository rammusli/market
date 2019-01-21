from  django.db import  models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add='True',verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now='True',verbose_name='更新时间')
    is_delete = models.BooleanField(default= False,verbose_name= '是否删除') #假删除

    class Meta:
        #定义模型类，不会被迁移
        abstract = True
