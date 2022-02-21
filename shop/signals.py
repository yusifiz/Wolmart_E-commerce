from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Shop, ProductCategory
from django.template.defaultfilters import slugify

@receiver(post_save, sender=Shop)
def save_shop(sender, created, instance, **kwargs):
    if created:
        instance.slug = slugify(instance.name + "-" + str(instance.created_at))
        instance.save()
        
        
@receiver(post_save, sender=ProductCategory)
def save_shop(sender, created, instance, **kwargs):
    if created:
        instance.slug = slugify(instance.name)
        instance.save()