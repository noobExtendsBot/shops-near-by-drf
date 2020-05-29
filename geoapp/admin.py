from django.contrib import admin
from .models import Shop
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.




class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

admin.site.register(Shop, ShopAdmin)