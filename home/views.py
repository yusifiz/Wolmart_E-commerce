from unicodedata import category
from django.shortcuts import render
from blog.models import Blog
from shop.models import Shop
# Create your views here.

def index(request):
    product = Shop.objects.filter(category__name='t-shirt').order_by('-created_at')[:5]
    

    blog_list = Blog.objects.all()[:5]
    context = {
        'blog_list' : blog_list,
        'product':product
    }
    return render(request, "index.html", context)