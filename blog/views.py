# from gc import get_objects
from django.shortcuts import render
from . models import Blog, BlogCategory, BlogTag
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import BlogCommentForm
from .models import Comment
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
    form = BlogCommentForm
    

    def post(self, request, *args, **kwargs):
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse_lazy('blog:single_blog', kwargs={
                'slug':post.slug
            }))

    
    def get_context_data(self, **kwargs):
        post_comments = Comment.objects.all().filter(post=self.object.id)
        comment_count = Comment.objects.all().filter(post=self.object.id).count()
        recent_blogs = Blog.objects.order_by('-created_at')[:3]
        blog = Blog.objects.all()
        related_blogs = Blog.objects.filter(category = self.object.category).exclude(name = self.object.name)
        # tags = BlogTag.objects.filter(name=self.get_object())
        # print(self.kwargs.get('tag'))
        context = super().get_context_data(**kwargs)
        context.update({
            'recent_blogs':recent_blogs,
            'related_blogs':related_blogs,
            'form': self.form,
            'comment': post_comments,
            'count': comment_count,
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