from django.shortcuts import render
from . models import Blog, BlogCategory
from django.views.generic import ListView, DetailView
# Create your views here.

class BlogListView(ListView):
    model = Blog
    template_name = 'blog.html'
    paginate_by = 3 
    

# def blog_mask_masonry(request):
#     return render(request, "blog-mask-masonry.html")

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post-single.html'
    context_object_name = 'blog_detail'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
def blog_filter(request, slug):
    blog = Blog.objects.filter(category__slug=slug)
    blogCategory = BlogCategory.objects.all()
    context = {
        'blog':blog,
        'blogCategory':blogCategory,
    }
    return render(request, 'blog_filter.html', context)

