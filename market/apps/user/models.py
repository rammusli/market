from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from db.base_model import BaseModel

'''用户模型'''
class User(BaseModel):
    #用户对象属性
    gender_choices=(
        (1,"男"),
        (2,"女"),
        (3,"保密"),
    )
    # user_head = models.ImageField(upload_to='user', verbose_name='头像', default='user/10.jpg', max_length=500)
    user_phone = models.CharField(max_length=11,
                                  verbose_name= "手机号码",
                                  validators=[RegexValidator(r'^1[3-9]\d{9}$',"手机格式错误")])
    user_nickname = models.CharField(max_length=20,
                                     verbose_name='用户名',
                                     null=True,
                                     blank=True) # 用户名
    user_password = models.CharField(max_length=16,
                                     verbose_name='密码')
    user_birth = models.DateField(verbose_name= "生日",
                                  null=True,
                                  blank=True)
    user_gender = models.SmallIntegerField(choices=gender_choices,
                                           default=3,
                                           verbose_name= '性别')
    user_school = models.CharField(max_length=40,
                                   verbose_name="学校",
                                   null=True,
                                   blank=True)
    user_address = models.CharField(max_length=40,
                                    verbose_name="地址",
                                    null=True,
                                    blank=True)
    user_hometown = models.CharField(max_length=43,
                                     verbose_name="籍贯",
                                     null=True,
                                     blank=True)

    def __str__(self):
        return  self.user_nickname
