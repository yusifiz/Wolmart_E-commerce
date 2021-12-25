from django.urls import path
from .views import BlogListView,post_single

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('single-blog/', post_single, name='single_blog'),
]