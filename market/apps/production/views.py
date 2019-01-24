from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# 商品首页
from production.models import ProSKU


class IndexView(View):
    # def post(self,request):
    #     return HttpResponse('商品首页post')
    def get(self,request):
        return render(request,'production/index.html')




# 商品分类(商品列表)
class CategoryView(View):
    # def post(self,request):
    #     return HttpResponse('商品分类post')
    def get(self,request):
        return render(request,'production/category.html')





# 商品详情
class DetailView(View):
    # def post(self,request):
    #     return HttpResponse('商品分类post')
    def get(self,request):
        prosku = ProSKU.objects.get(pk=id)

        # 渲染数据到页面
        context = {
            "prosku": prosku
        }
        return render(request,'production/detail.html')



