from modeltranslation.translator import translator, TranslationOptions
from .models import Shop


class ShopTranslationOptions(TranslationOptions):
    fields = ('description','name')
    
translator.register(Shop, ShopTranslationOptions)