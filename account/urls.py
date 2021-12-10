from django.urls import path
from .views import login, my_account

app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    path('my-account/', my_account, name='my_account'),
]