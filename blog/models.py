from django.db import models
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from account.models import User
# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)


    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'
        
    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE,max_length=127, null=True, blank=True)
    tags = TaggableManager()
    name = models.CharField(max_length=127, blank=True, null=True)
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=127, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    content = RichTextField(help_text='Content', null=True, blank=True)
    author_comment = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)
    
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ('created_at',)
    
    def __str__(self):
        return self.name
    
    
class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return (self.name)
    
