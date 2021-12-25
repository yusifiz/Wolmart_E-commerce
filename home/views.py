from django.shortcuts import render
from blog.models import Blog
# Create your views here.

def index(request):
    blog_list = Blog.objects.all()
    context = {
        'blog_list' : blog_list
    }
    return render(request, "index.html", context)