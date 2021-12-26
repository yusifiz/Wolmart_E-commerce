from django.db import models

# Create your models here.

class Shop(models.Model):
    category = models.CharField(max_length=127, null=True, blank=True)
    name = models.CharField(max_length=127, null=True, blank=True)
    price1 = models.SmallIntegerField(null=True, blank=True)
    price2 = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to='shop/')
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('created_at',)
        
    def __str__(self):
        return self.name