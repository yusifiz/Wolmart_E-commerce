from django.urls import path
from .views import product_gallery,shop

app_name = 'product'

urlpatterns = [
    path('single-product/', product_gallery, name='single_product'),
    path('', shop, name='shop'),
]