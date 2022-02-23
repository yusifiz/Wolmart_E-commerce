from django.urls import path
from .views import BlogListView,BlogDetailView, blog_filter

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<slug:slug>', BlogDetailView.as_view() , name='single_blog'),
    path('blog-filter/<slug:slug>',blog_filter,name='blog_filter'),

]