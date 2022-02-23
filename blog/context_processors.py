from .models import BlogCategory

def global_blog_category(request):
    blog_category = BlogCategory.objects.all()
    context={
        'blog_category':blog_category,
    }
    return context