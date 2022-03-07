from modeltranslation.translator import translator, TranslationOptions
from .models import Shop


class ShopTranslationOptions(TranslationOptions):
    fields = ()
    
translator.register(Shop, ShopTranslationOptions)