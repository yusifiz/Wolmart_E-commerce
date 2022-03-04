from django.contrib import admin
from . models import Shop, Order, OrderItem, ProductCategory, Brand, Color, Wishlist, WishlistItem, Size, Checkout
# Register your models here.

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    fields = ('category','name', 'image', 'price','color','brand','size','description')
    

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    fields = ('name','image',)
    
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
admin.site.register(Size)
admin.site.register(Checkout)
