from django.contrib import admin

#Register your models here.
from .models import ProCategory, ProductUnit, ProSPU,  ProSKU, PhotoAlbum,  Banner, Activity, ActivityRegion

admin.site.register(ProCategory)
admin.site.register(ProductUnit)
admin.site.register(ProSPU)
admin.site.register(ProSKU)
admin.site.register(PhotoAlbum)
admin.site.register(Banner)
admin.site.register(Activity)
admin.site.register(ActivityRegion)
#

