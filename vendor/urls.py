from django.urls import path
from .views import vendor_dokan_store,vendor_wcfm_store

app_name = 'vendor'

urlpatterns = [
    path('', vendor_wcfm_store, name='vendor'),
    path('single-vendor/', vendor_dokan_store, name='single_vendor'),
]