from django.db import models

from account.models import User

# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(upload_to='banner/', null=True, blank=True)

    def __str__(self):
        return self.title

class Color(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
class Brand(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return self.size
    
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    image = models.ImageField(upload_to='productCategory/', null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        
    def __str__(self):
        return self.name


class Shop(models.Model):
    
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE,max_length=127, null=True, blank=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,max_length=127, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,max_length=127, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,max_length=127, null=True, blank=True)
    name = models.CharField(max_length=127, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    discount_percent = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='shop/')
    image2 = models.ImageField(null=True,blank=True,upload_to='shop/')
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('created_at',)
        
    @property
    def calculate_discount(self):
        if self.discount_percent > 0:
            return self.price - (self.price*self.discount_percent)/100
        return self.price
        
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True)
    
    # def __str__(self):
    #     return self.id
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.product
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True)
    
    # def __str__(self):
    #     return self.id
    
    
class WishlistItem(models.Model):
    product = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.product
    
class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    adress1 = models.CharField(max_length=255, null=True, blank=True)
    items = models.ForeignKey(OrderItem, on_delete=models.CASCADE, null=True, blank=True)
    adress2 = models.CharField(max_length=255, null=True, blank=True)
    town = models.CharField(max_length=255, null=True, blank=True)
    zip = models.CharField(max_length=255, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    
    # def __str__(self):
    #     return self.id