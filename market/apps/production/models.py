from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
from db.base_model import BaseModel
from ckeditor_uploader.fields import RichTextUploadingField

class ProCategory(BaseModel):
    """
    商品分类
    ID
    分类名
    分类简介

    """
    category_name = models.CharField(max_length=32,
                                     verbose_name='分类名')
    category_introduce = models.CharField(max_length=200,
                                          verbose_name='分类简介',
                                          null=True,
                                          blank=True)
    category_order = models.SmallIntegerField(default=0,
                                              verbose_name="排序")

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "分类管理"
        verbose_name_plural = verbose_name

class ProSPU(BaseModel):
    """
        商品SPU表
        ID
        名称
        详情
    """
    spu_name = models.CharField(max_length=32,
                                verbose_name='商品spu名')
    spu_introduce = RichTextUploadingField(verbose_name='商品spu详情')

    def __str__(self):
        return self.spu_name

    class Meta:
        verbose_name = "商品SPU管理"
        verbose_name_plural = verbose_name

class ProSKU(BaseModel):
    """
        商品SKU表
    """
    SHOW_STATUS_CHOICES = (
        (1, '上架'),
        (2, '下架'),
    )
    sku_name = models.CharField(max_length=100,
                                verbose_name='商品名')
    sku_introduce = RichTextUploadingField(verbose_name='商品简介',
                                           null=True,
                                           blank=True)
    sku_price = models.DecimalField(max_digits=9,
                                    decimal_places=2,
                                    verbose_name="商品价格",
                                    default=0,)
    sku_unit = models.ForeignKey(to="ProductUnit", verbose_name="单位")
    sku_inventory = models.IntegerField(verbose_name='商品库存',
                                        default=0)
    sku_sales_volume = models.IntegerField(verbose_name='商品销量',
                                           null=True,
                                           blank=True)
    sku_logo = models.ImageField(upload_to='pro_logo',
                                 verbose_name='商品LOGO地址',
                                 null=True,
                                 blank=True,
                                 max_length=500)
    sku_show = models.IntegerField(choices=SHOW_STATUS_CHOICES,
                                   verbose_name='上架状态',
                                   default=1)
    sku_category_id = models.ForeignKey(to='ProCategory',
                                        on_delete=models.CASCADE,
                                        verbose_name="商品分类id")
    sku_spu_id = models.ForeignKey(to='ProSPU',
                                   on_delete=models.CASCADE,
                                   verbose_name="商品spuid")

    def __str__(self):
        return self.sku_name

    class Meta:
        verbose_name = "商品SKU管理"
        verbose_name_plural = verbose_name




class PhotoAlbum(BaseModel):
    """
        商品相册
        ID
        图片地址
        商品SKUID

    """
    photo_url = models.ImageField(upload_to='pro_photo',
                                  verbose_name='图片地址',
                                  null=True,
                                  blank=True)
    photo_sku_id = models.ForeignKey(to='ProSKU',
                                     on_delete=models.CASCADE,
                                     verbose_name="图片sku_id")

    def __str__(self):
        return self.photo_url.__str__()

    class Meta:
        verbose_name = "商品相册管理"
        verbose_name_plural = verbose_name


class ProductUnit(BaseModel):
    """
        商品单位表
        ID
        单位名（斤，箱）

    """
    unit_name = models.CharField(max_length=10,
                                 verbose_name="商品单位",
                                 null= True,
                                 blank=True)

    def __str__(self):
        return self.unit_name

    class Meta:
        verbose_name = "商品单位管理"
        verbose_name_plural = verbose_name


class Banner(BaseModel):
    """
    首页轮播商品
    ID
    名称
    商品SKUID
    图片地址
    排序（order）

    """
    banner_name = models.CharField(max_length=32, verbose_name="轮播图名字")
    banner_sku_id = models.ForeignKey(to='ProSKU', on_delete=models.CASCADE, verbose_name="轮播sku_id")
    banner_url = models.ImageField(upload_to='banner', verbose_name='轮播图片地址', null=True, blank=True, max_length=500)
    banner_order = models.IntegerField(null=True, blank=True, verbose_name="排序")

    def __str__(self):
        return self.banner_name

    class Meta:
        verbose_name = "轮播图管理"
        verbose_name_plural = verbose_name


class Activity(models.Model):
    """
        首页活动表
        ID
        名称
        图片地址
        url地址 www.jd.com
    """
    activity_name = models.CharField(max_length=22, verbose_name="活动名字")
    activity_photo = models.ImageField(upload_to='activity', verbose_name='活动图片地址', null=True, blank=True,
                                       max_length=500)
    activity_address = models.URLField(max_length=500, verbose_name="活动链接地址")

    def __str__(self):
        return self.activity_name

    class Meta:
        verbose_name = "活动管理"
        verbose_name_plural = verbose_name


class ActivityRegion(BaseModel):
    """
        首页活动专区
        ID
        名称
        描述
        排序
        是否上架
        专区ID

    """
    SHOW_STATUS_CHOICES = (
        (1, '上架'),
        (2, '下架'),
    )
    region_name = models.CharField(max_length=22, verbose_name="专区名字")
    region_introduce = models.CharField(max_length=22,verbose_name="专区描述")
    region_order = models.IntegerField(verbose_name="专区排序")
    region_show = models.IntegerField(choices=SHOW_STATUS_CHOICES, verbose_name="上架状态", default=1)
    region_sku = models.ManyToManyField(ProSKU,verbose_name='商品')


    def __str__(self):
        return self.region_name

    class Meta:
        verbose_name = "活动专区管理"
        verbose_name_plural = verbose_name




