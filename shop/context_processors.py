from . models import Shop

def global_shop(request):
    products = Shop.objects.all()
    context = {
        'products':products
    }
    return context