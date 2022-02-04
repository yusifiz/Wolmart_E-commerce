from django.urls import path
from .views import ShopListView, ShopDetailView, update_item, cart, checkout

app_name = 'product'

urlpatterns = [
    path('<slug:slug>', ShopDetailView.as_view(), name='single_product'),
    path('', ShopListView.as_view(), name='shop'),
    path('update_item/', update_item, name="update_item"),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]