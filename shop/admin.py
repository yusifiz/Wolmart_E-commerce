from django.contrib import admin
from . models import Shop, Order, OrderItem, ProductCategory, Brand, Color
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'image', 'price','color','brand','size',)
    

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Brand)
admin.site.register(Color)