from django.shortcuts import render

# Create your views here.

def become_a_vendor(request):
    return render(request, "become-a-vendor.html")

def compare(request):
    return render(request, "compare.html")

def error_404(request):
    return render(request, "error-404.html")

def faq(request):
    return render(request, "faq.html")

def order_view(request):
    return render(request, "order-view.html")

def order(request):
    return render(request, "order.html")

