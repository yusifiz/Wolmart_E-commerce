from django.urls import path
from .views import become_a_vendor,compare,error_404,faq,order,order_view

app_name = 'pages'

urlpatterns = [
    path('become-a-vendor/', become_a_vendor, name='become_a_vendor'),
    path('compare/', compare, name='compare'),
    path('error-404/', error_404, name='error_404'),
    path('faq/', faq, name='faq'),
    path('order/', order, name='order'),
    path('order-view/', order_view, name='order_view'),

]