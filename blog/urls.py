from django.urls import path
from .views import blog_mask_masonry,post_single

app_name = 'blog'

urlpatterns = [
    path('', blog_mask_masonry, name='blog'),
    path('single-blog/', post_single, name='single_blog'),
]