from django.contrib import admin

from blog.translation import BlogTranslationOptions
from . models import Blog
from modeltranslation.translator import translator, TranslationOptions, register

# Register your models here.
admin.site.register(Blog)


# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     fields = ('category', 'name', 'image', 'author', 'content', 'author_comment')
    

# @register(Blog)
# class BlogTranslationOptions(TranslationOptions)