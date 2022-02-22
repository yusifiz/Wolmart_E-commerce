from tabnanny import verbose
from unicodedata import category
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(max_length=127, null=True, blank=True)
    slug = models.SlugField(max_length=127, null=True, blank=True)


    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

class Blog(models.Model):
    category = models.CharField(max_length=127, blank=True, null=True)
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