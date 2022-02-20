from django.urls import path
from . views import  SubscriberAPIView

app_name = 'home'

urlpatterns = [
    path('', SubscriberAPIView.as_view(), name='subscribe'),
]