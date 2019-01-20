from django.db import models

# Create your models here.
class User(models.Model):
    sex_choices=((1,"男"),(2,"女"),(3,"保密"),)
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    Gender = models.SmallIntegerField(choices=sex_choices,default=3)
    is_delete = models.BooleanField(default= False) #假删除
