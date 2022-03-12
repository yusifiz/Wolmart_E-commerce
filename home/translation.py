from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider, ServiceSlider


class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')

translator.register(HomeSlider, HomeTranslationOptions) 

class ServiceSliderTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')
    
translator.register(ServiceSlider, ServiceSliderTranslationOptions)