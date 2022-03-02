from unicodedata import category
from django.shortcuts import render
from blog.models import Blog
from shop.models import Shop
# Create your views here.

def index(request):
    product = Shop.objects.filter(category__name='t-shirt').order_by('-created_at')[:5]
    deals_hot = Shop.objects.filter(price__range=(0, 101)).order_by("-created_at")[:2]
    clothes = Shop.objects.filter(category__name__in=['Clothes', 'Wear','T-shirt'])
    electronics = Shop.objects.filter(category__name__in=['Electronics', 'Computer','Phone'])
    blog_list = Blog.objects.all()[:5]
    context = {
        'blog_list' : blog_list,
        'product':product,
        'deals_hot':deals_hot,
        'clothes':clothes,
        'electronics':electronics,
    }
    return render(request, "index.html", context)