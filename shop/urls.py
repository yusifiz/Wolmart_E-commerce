from django.urls import path
from .views import ShopListView, ShopDetailView, cart, checkout, update_item, search_bar, filter, filter_data, wishlist, wishlist_view

app_name = 'product'

urlpatterns = [
    path('<slug:slug>', ShopDetailView.as_view(), name='single_product'),
    path('', ShopListView.as_view(), name='shop'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('update_item/', update_item, name="update_item"),
    path('cart/update_item/', update_item, name="update_item"),
    path('search/update_item/', update_item, name="update_item"),   
    path('search/wishlist/', wishlist, name="add_wishlist"),   
    path('search/', search_bar, name='search'),
    path('filter/<slug:slug>', filter, name='filter'),
    # path('filter/<slug:slug>/filter-data/', filter_data, name='filter_data'),
    path('filter-data/',filter_data,name='filter_data'),
    # path('filter-data/update_item/', update_item, name="update_item"),
    path('wishlist/', wishlist, name='add_wishlist'),
    path('wishlistview/', wishlist_view, name='wishlist_view'),
    path('wishlistview/wishlist/', wishlist, name='add_wishlist'),
    
]