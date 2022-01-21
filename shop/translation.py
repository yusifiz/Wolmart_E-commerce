from modeltranslation.translator import translator, TranslationOptions
from .models import Shop


class ShopTranslationOptions(TranslationOptions):
    fields = ('name','category')
    
translator.register(Shop, ShopTranslationOptions)