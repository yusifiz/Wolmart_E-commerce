from django.shortcuts import render
from . models import Blog, BlogCategory, BlogTag
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
        recent_blogs = Blog.objects.order_by('-created_at')[:3]
        blog = Blog.objects.all()
        related_blogs = Blog.objects.filter(category = self.object.category).exclude(name = self.object.name)
        # tags = BlogTag.objects.filter(name=self.get_object())
        # print(self.kwargs.get('tag'))
        context = super().get_context_data(**kwargs)
        context.update({
            'recent_blogs':recent_blogs,
            'related_blogs':related_blogs,
            # 'tags':tags,
        })
        return context
    
    
def blog_filter(request, slug):
    blog = Blog.objects.filter(category__slug=slug)
    blogCategory = BlogCategory.objects.all()
    context = {
        'blog':blog,
        'blogCategory':blogCategory,
    }
    return render(request, 'blog_filter.html', context)

def blog_search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        search_item = Blog.objects.filter(name__icontains = searched)
        
        return render(request, 'search_blog.html',{'searched':searched,'search_item':search_item})
    else:
        return render(request,'search_blog.html',{})