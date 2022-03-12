
from django.contrib import admin
from .models import Subscriber, HomeSlider, ServiceSlider
# Register your models here.

admin.site.register(Subscriber)
@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    exclude = ('title','desc')
    fileds = ('title_az','title_en', 'desc_az', 'desc_en', 'image',)
    
    
@admin.register(ServiceSlider)
class ServiceSliderAdmin(admin.ModelAdmin):
    exclude = ('title','desc')
    fileds = ('title_az','title_en', 'desc_az', 'desc_en', 'icon',)