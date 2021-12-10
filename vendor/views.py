from django.shortcuts import render

# Create your views here.

def vendor_dokan_store(request):
    return render(request, "vendor-dokan-store.html")


def vendor_wcfm_store(request):
    return render(request, "vendor-wcfm-store.html")