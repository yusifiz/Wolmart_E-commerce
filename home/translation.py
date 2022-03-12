from modeltranslation.translator import translator, TranslationOptions
from .models import HomeSlider


class HomeTranslationOptions(TranslationOptions):
    fields = ('title', 'desc')

translator.register(HomeSlider, HomeTranslationOptions) 