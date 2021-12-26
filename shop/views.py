from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Shop
# Create your views here.

class ShopListView(ListView):
    model = Shop
    template_name = 'shop.html'
    paginate_by = 12
    context_object_name = 'products'
    # queryset = Shop.objects.filter(is_active=True)
    
    
    
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