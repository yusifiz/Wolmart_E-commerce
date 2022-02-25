from django.urls import path
from .views import BlogListView,BlogDetailView, blog_filter, blog_search_bar, TagIndexView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('<slug:slug>', BlogDetailView.as_view() , name='single_blog'),
    path('blog-filter/<slug:slug>',blog_filter,name='blog_filter'),
    path('search/', blog_search_bar, name='blog_search'),
    path('tags/<slug:tag_slug>/',TagIndexView.as_view(), name='posts_by_tag'),
]