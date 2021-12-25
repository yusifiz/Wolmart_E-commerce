from django.shortcuts import render
from . models import Blog
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 3 


# def blog_mask_masonry(request):
#     return render(request, "blog-mask-masonry.html")

def post_single(request):
    return render(request, "post-single.html")