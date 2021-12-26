from django.urls import path
from .views import ShopListView, ShopDetailView

app_name = 'product'

urlpatterns = [
    path('<int:pk>', ShopDetailView.as_view(), name='single_product'),
    path('', ShopListView.as_view(), name='shop'),
]