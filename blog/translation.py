from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ('name', 'category', 'content')
    
translator.register(Blog, BlogTranslationOptions)