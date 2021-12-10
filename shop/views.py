from django.shortcuts import render

# Create your views here.

def product_gallery(request):
    return render(request, "product-gallery.html")

def shop(request):
    return render(request, "shop-grid-3cols.html")