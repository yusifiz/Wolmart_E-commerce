from modeltranslation.translator import translator, TranslationOptions
from .models import Shop


class ShopTranslationOptions(TranslationOptions):
    fields = ('name','category','description')
    
translator.register(Shop, ShopTranslationOptions)