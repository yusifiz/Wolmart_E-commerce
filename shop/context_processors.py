from . models import Shop, ProductCategory, Color

# def global_shop(request):
#     products = Shop.objects.all()
#     context = {
#         'products':products
#     }
#     return context


def global_product_category(request):
    product_category = ProductCategory.objects.all()
    colors = list(Color.objects.all().values_list('id', flat=True))
    context={
        'product_category':product_category,
        'color':colors
    }
    return context