from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from . models import Shop, Order, OrderItem, ProductCategory, Color,Brand

# Create your views here.

class ShopListView(ListView):
    model = Shop
    template_name = 'shop.html'
    paginate_by = 12
    context_object_name = 'products'
    # queryset = Shop.objects.filter(is_active=True)
    def get_context_data(self, **kwargs):
        categories = ProductCategory.objects.all()
        size = list(Shop.objects.all().values_list('size', flat=True))
        color = Color.objects.all()
        brand = Brand.objects.all()
        context = super().get_context_data(**kwargs)
        print(size)
        context.update({
            'categories':categories,
            # 'size':size,
            'color':color,
            'brand':brand,
        })
        return context
    
    
class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop-detail.html'
    context_object_name = 'product'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Test user'
        return context


# def product_gallery(request):
#     return render(request, "product-gallery.html")

# def shop(request):
#     return render(request, "shop-grid-3cols.html")


def cart(request):
    
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, status=False)
        items = order.orderitem_set.all()
        
        
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        
    context = {
        'items': items,
        'order':order
    }
    return render(request, 'cart.html', context)

def base_cart(request):
    
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, status=False)
        items = order.orderitem_set.all()
        cartItems = order['get_cart_items']
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    context = {
        'items': items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request, 'base.html', context)

def checkout(request):
    
    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, status=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

        
    context = {
        'items': items,
        'order':order
        
    }
    return render(request, 'checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Action', action)
    print('ProductID', productID)
    
    user = request.user.id
    product = Shop.objects.get(id=productID)
    order, created = Order.objects.get_or_create(user=user, status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0 or action == 'removeAll':
        orderItem.delete()
    # elif action == 'removeCart':
    #     order.delete()
    return JsonResponse('item was added', safe=False)


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_item = Shop.objects.filter(name__icontains = searched)
        
        return render(request, 'search.html',{'searched':searched,'search_item':search_item})
    else:
        return render(request,'search.html',{})
    
    
def filter(request, slug):
    product = Shop.objects.filter(category__slug=slug)
    category = ProductCategory.objects.filter(slug=slug).first()
    context = {
        'product':product,
        'category':category,
    }
    return render(request, 'filter.html', context)


def filter_data(request):

    color = request.GET.getlist('color[]')
    brand = request.GET.getlist('brand[]')
    # color = list(Color.objects.all().values_list('id', flat=True))
    
    allprod=Shop.objects.all()
    print(color)
    if len(color)>0:
        print('salam')
        
        allprod=allprod.filter(color__name__in = color)
        print(allprod)
    if len(brand)>0:
        print('sagol')
        
        allprod=allprod.filter(brand__name__in = brand)
        print(allprod)
        
    t = render_to_string('ajax/shop-filter.html', {'data': allprod})
        # print(t)
    return JsonResponse({'data':t})