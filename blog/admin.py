from django.contrib import admin
from . models import Blog
# Register your models here.



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('category', 'name', 'image', 'author', 'content', 'author_comment')