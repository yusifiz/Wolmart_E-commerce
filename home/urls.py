from django.urls import path
from .views import index
from shop.views import update_item, wishlist
app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('update_item/', update_item, name='update_item'),
    path('wishlist/', wishlist, name='add_wishlist'),
]