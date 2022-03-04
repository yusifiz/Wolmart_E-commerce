from django.contrib import admin

from blog.translation import BlogTranslationOptions
from . models import Blog, BlogCategory, Comment
from modeltranslation.translator import translator, TranslationOptions, register

# Register your models here.
# admin.site.register(Blog)

admin.site.register(Comment)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    fields = ('name',)
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('category', 'name_az','name_en', 'image', 'author', 'content_az','content_en', 'author_comment','tags')
    

# @register(Blog)
# class BlogTranslationOptions(TranslationOptions)