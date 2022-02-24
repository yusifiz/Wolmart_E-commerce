from django.contrib import admin

from blog.translation import BlogTranslationOptions
from . models import Blog, BlogCategory, BlogTag, Comment
from modeltranslation.translator import translator, TranslationOptions, register

# Register your models here.
admin.site.register(Blog)

admin.site.register(Comment)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    
    
@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    fields = ('name',)

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     fields = ('category', 'name', 'image', 'author', 'content', 'author_comment')
    

# @register(Blog)
# class BlogTranslationOptions(TranslationOptions)