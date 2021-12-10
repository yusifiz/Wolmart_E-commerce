from django.shortcuts import render

# Create your views here.

def blog_mask_masonry(request):
    return render(request, "blog-mask-masonry.html")

def post_single(request):
    return render(request, "post-single.html")