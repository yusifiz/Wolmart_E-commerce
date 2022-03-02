from unicodedata import category
from django.shortcuts import render
from blog.models import Blog
from shop.models import Shop
# Create your views here.

def index(request):
    # product = Shop.objects.filter(category__name='t-shirt').order_by('-created_at')[:5]
    deals_hot = Shop.objects.filter(price__range=(0, 101)).order_by("-created_at")[:2]
    clothes = Shop.objects.filter(category__name__in=['Clothes', 'Wear','T-shirt'])[:5]
    furniture = Shop.objects.filter(category__name__in=['Furniture', 'Cup'])[:5]
    electronics = Shop.objects.filter(category__name__in=['Electronics', 'Computer','Phone'])[:5]
    best_selling = Shop.objects.all().filter(category__name__in=['Electronics', 'Computer','Phone']).order_by('-id')[:3]
    sale_product = Shop.objects.all().filter(category__name__in=['Clothes', 'Wear','T-shirt']).order_by('-id')[:3]
    featured = Shop.objects.all().filter(category__name__in=['Furniture', 'Cup']).order_by('-id')[:3]
    blog_list = Blog.objects.all()[:5]
    context = {
        'blog_list' : blog_list,
        # 'product':product,
        'deals_hot':deals_hot,
        'clothes':clothes,
        'electronics':electronics,
        'furniture':furniture,
        'best_selling':best_selling,
        'sale_product':sale_product,
        'featured':featured
    }
    return render(request, "index.html", context)