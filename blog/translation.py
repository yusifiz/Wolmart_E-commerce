from modeltranslation.translator import translator, TranslationOptions
from .models import Blog


class BlogTranslationOptions(TranslationOptions):
    fields = ('name', 'content')
    
translator.register(Blog, BlogTranslationOptions)