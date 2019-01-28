from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

# 商品首页
from production.models import ProSKU, ProCategory, Banner, Activity, ActivityRegion


class IndexView(View):
    def get(self,request):
        """首页"""
        # 获取轮播
        banners = Banner.objects.filter(is_delete=False).order_by("-order")

        # 获取活动
        acts = Activity.objects.filter(is_delete=False)

        # 获取特色专区
        act_zones = ActivityRegion.objects.filter(region_show =1, is_delete=False).order_by("-order")

        # 渲染数据
        context = {
            "banners": banners,
            "acts": acts,
            "act_zones": act_zones,
        }

        return render(request, "production/index.html", context)





# 商品分类(商品列表)
class CategoryView(View):

    def get(self,request,cate_id,order):
        try:
            cate_id = int(cate_id)
            order = int(order)
        except:
            return redirect("production:index")

        # 所有的分类 产品经理
        categorys = ProCategory.objects.filter(is_delete=False).order_by("-order")

        # 查询某个分类下的所有商品
        # 默认查询第一个分类
        if cate_id == 0:
            category = categorys.first()
            cate_id = category.pk

        goodsSkus = ProSKU.objects.filter(sku_show=1, is_delete=False , sku_category_id=cate_id)

        order_rule = ["id", "-sku_sales_volume", "-sku_price", "sku_price", "-create_time"]
        try:
            order_one = order_rule[order]
        except:
            order_one = order_rule[0]
            order = 0
        goodsSkus = goodsSkus.order_by(order_one)
        return render(request,'production/category.html')





# 商品详情
class DetailView(View):

    def get(self,request):
        prosku = ProSKU.objects.get(pk=id)

        # 渲染数据到页面
        context = {
            "prosku": prosku
        }
        return render(request,'production/detail.html')



