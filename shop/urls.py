from django.urls import path
from .views import ShopListView, ShopDetailView, cart, checkout, update_item, search_bar

app_name = 'product'

urlpatterns = [
    path('<slug:slug>', ShopDetailView.as_view(), name='single_product'),
    path('', ShopListView.as_view(), name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name="update_item"),
    path('cart/update_item/', update_item, name="update_item"),
    path('search/', search_bar, name='search')
]