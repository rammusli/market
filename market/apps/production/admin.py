from django.contrib import admin

#Register your models here.
from .models import ProCategory, ProductUnit, ProSPU,  ProSKU, PhotoAlbum,  Banner, Activity, ActivityRegion

class ArtcleAdimin(admin.ModelAdmin):
    list_display = ('id','category_name','category_introduce','category_order','create_time','update_time')
    ordering = ('-id',)
admin.site.register(ProCategory,ArtcleAdimin)
admin.site.register(ProductUnit)
admin.site.register(ProSPU)
admin.site.register(ProSKU)
admin.site.register(PhotoAlbum)
admin.site.register(Banner)
admin.site.register(Activity)
admin.site.register(ActivityRegion)
#

