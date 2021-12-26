from django.contrib import admin
from . models import Shop
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'image', 'price1', 'price2')