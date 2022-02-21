from . models import Shop, ProductCategory

def global_shop(request):
    products = Shop.objects.all()
    context = {
        'products':products
    }
    return context


def global_product_category(request):
    product_category = ProductCategory.objects.all()
    context={
        'product_category':product_category,
    }
    return context