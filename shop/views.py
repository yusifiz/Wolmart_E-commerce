from importlib import import_module
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse
import json
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.db.models import Q

from shop.forms import CheckoutForm
from . models import Shop, Order, OrderItem, ProductCategory, Color,Brand, Size, Wishlist, WishlistItem

# Create your views here.

class ShopListView(ListView):
    model = Shop
    template_name = 'shop.html'
    paginate_by = 12
    context_object_name = 'products'
    # queryset = Shop.objects.filter(is_active=True)
    def get_context_data(self, **kwargs):
        categories = ProductCategory.objects.all()
        size = Size.objects.all()
        color = Color.objects.all()
        brand = Brand.objects.all()
        context = super().get_context_data(**kwargs)
        # print(size)
        context.update({
            'categories':categories,
            'size':size,
            'color':color,
            'brand':brand,
        })
        return context
    
    
class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shop-detail.html'
    context_object_name = 'product'
    

    def get_context_data(self, **kwargs):
        categories = ProductCategory.objects.all()
        size = Size.objects.all()
        color = Color.objects.all()
        brand = Brand.objects.all()
        # product = Shop.objects.all()
        related_product = Shop.objects.filter(category=self.object.category).exclude(name=self.object.name)
        more_product = Shop.objects.all().order_by('-id')[:3]
        context = super().get_context_data(**kwargs)
        context.update({
            'categories':categories,
            'size':size,
            'color':color,
            'brand':brand,
            'related_product':related_product,
            'more_product':more_product,
            # 'product':product,
        })
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
        print(items)
        
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
        # print('base -----.',items)
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

# def checkout(request):
    
#     if request.user.is_authenticated:
#         user = request.user
#         order, created = Order.objects.get_or_create(user=user, status=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []
#         order = {'get_cart_total':0, 'get_cart_items':0}

        
#     context = {
#         'items': items,
#         'order':order
        
#     }
#     return render(request, 'checkout.html', context)

def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']
    print('Actionnnnn', action)
    print('ProductID', productID)
    # o = OrderItem.objects.all()
    user = request.user
    product = Shop.objects.get(id=productID)
    order, created = Order.objects.get_or_create(user=user, status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    oitemcount = OrderItem.objects.all().count()
    print("orderItem.quantity")
    if action == 'addCart':
        orderItem.quantity = (orderItem.quantity + 1)
        print(orderItem.quantity)
    elif action == 'removeCart':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0 or action == 'removeAll':
        orderItem.delete()
        print(oitemcount)
        
    if action=='removeOrder':
        order.delete()
    
    if oitemcount <= 1 and (action == 'removeAll' or action == 'remove'):
        order.delete()
    # elif o.quantity <= 0:
    #     order.delete()

    # elif action == 'removeCart':
    #     order.delete()
    return JsonResponse('item was added', safe=False)


def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_item = Shop.objects.filter(
        Q(name__icontains=searched) | Q(description__icontains=searched)
    )   
        # if searched in str(list(search_item)):
        #     print( searched, search_item)
        #     return render(request, 'search.html',{'searched':searched,'search_item':search_item})
        # else:
        #     print( searched, search_item)
        #     return redirect(reverse_lazy('pages:error_404'))
        context = {
            'search_item':search_item,
            'searched':searched,
        }
        return render(request, 'search.html',context)
    
def filter(request, slug):
    product = Shop.objects.filter(category__slug=slug)
    category = ProductCategory.objects.filter(slug=slug).first()
    categories = ProductCategory.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    brand = Brand.objects.all()
    context = {
        'product':product,
        'category':category,
        'size':size,
        'color':color,
        'brand':brand,
        'categories':categories,
    }
    return render(request, 'filter.html', context)


def filter_data(request):

    color = request.GET.getlist('color[]')
    brand = request.GET.getlist('brand[]')
    size = request.GET.getlist('size[]')
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
    if len(size)>0:
        print('sagol')
        
        allprod=allprod.filter(size__size__in = size)
        print(allprod)
    t = render_to_string('ajax/shop-filter.html', {'data': allprod})
        # print(t)
    return JsonResponse({'data':t})


def wishlist(request):
    datas = json.loads(request.body)
    productID = datas['p']
    action = datas['a']
    print('Action', action)
    # print('ProductID', productID) 
    
    user = request.user
    product = Shop.objects.get(id=productID)
    wishlist, created = Wishlist.objects.get_or_create(user=user, status=False)
    wishlistitem, created = WishlistItem.objects.get_or_create(wishlist=wishlist, product=product)
    # oitemcount = OrderItem.objects.all().count()
    if action == 'addWishlist':
        wishlistitem.quantity = (wishlistitem.quantity + 1)
        # print(oitemcount)
        print('ProductID', productID)
    elif action == 'removeWishlist':
        # print('saasas')
        wishlistitem.quantity = 0
        
    wishlistitem.save()

    if wishlistitem.quantity == 0:
        # print('saasas')
        
        wishlistitem.delete()

    
    # if orderItem.quantity <= 0 or action == 'removeAll':
    #     orderItem.delete()
    #     print(oitemcount)
        
    # if oitemcount <= 1 and (action == 'removeAll' or action == 'remove'):
    #     order.delete()
        
     
    return JsonResponse('item was added', safe=False)


def wishlist_view(request):
        
    if request.user.is_authenticated:
        user = request.user
        wishlist, created = Wishlist.objects.get_or_create(user=user, status=False)
        items = wishlist.wishlistitem_set.all()
        # cartItems = order.get_cart_items
        
    else:
        items = []
        # order = {'get_cart_total': 0,'get_cart_items': 0 }
        # cartItems = order['get_cart_items']
        
        
        
    context = {
        'items': items,
        # 'order': order,
        # 'cartItems': cartItems
    }
    return render(request, 'wishlist.html', context)


def checkout(request):
    messageSent = False
    form = CheckoutForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CheckoutForm(data=request.POST)
            if form.is_valid():
                
                print(form)
                form.save()
                
                messageSent = True            
        user = request.user
        order, created = Order.objects.get_or_create(user=user, status=False)
        items = order.orderitem_set.all()
        print(items)
        cartItems = order.get_cart_items
        
    else:
        items = []
        order = {'get_cart_total': 0,'get_cart_items': 0 }
        cartItems = order['get_cart_items']
        
        
        
    context = {
        'items': items,
        'order': order,
        'cartItems':cartItems,
        'form':form,
        'messageSent':messageSent,
    }
    return render(request, 'checkout.html', context)