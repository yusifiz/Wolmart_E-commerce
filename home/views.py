from django.shortcuts import render
from blog.models import Blog
from shop.models import Shop
# Create your views here.

def index(request):
    product = Shop.objects.filter(price__range=(0, 101))[:2]


    blog_list = Blog.objects.all()
    context = {
        'blog_list' : blog_list,
        'product':product
    }
    return render(request, "index.html", context)