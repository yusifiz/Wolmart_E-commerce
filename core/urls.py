"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import  gettext_lazy as _

urlpatterns += i18n_patterns(
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), 
    path('',include("home.urls", namespace='home')),
    path('about/',include("about.urls", namespace="about")),
    path('account/',include("account.urls", namespace='account')),
    path('blog/',include("blog.urls", namespace='blog')),
    path('contact/',include("contact.urls", namespace='contact')),
    path('pages/',include("pages.urls", namespace='pages')),
    path('shop/',include("shop.urls", namespace='product')),
    path('vendor/',include("vendor.urls", namespace='vendor')),
    path('subscribe/', include('home.api.urls', namespace='home')),
    
    path('social-auth/', include('social_django.urls', namespace="social")),
    
)

