from . models import Shop, ProductCategory, Color, Brand

# def global_shop(request):
#     products = Shop.objects.all()
#     context = {
#         'products':products
#     }
#     return context


def global_product_category(request):
    product_category = ProductCategory.objects.all()
    colors = list(Color.objects.all().values_list('id', flat=True))
    brands = list(Brand.objects.all().values_list('id', flat=True))
    product = Shop.objects.all()
    context={
        'product_category':product_category,
        'color':colors,
        'product':product,
    }
    return context