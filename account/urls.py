from django.urls import path, re_path
from .views import login, my_account, register, activate

app_name = 'account'

urlpatterns = [
    path('login/', login, name='login'),
    path('my-account/', my_account, name='my_account'),
    path('register/', register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
]