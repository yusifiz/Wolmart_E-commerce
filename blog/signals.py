from django.db.models.signals import post_save
from django.dispatch import receiver
from . models import Blog
from django.template.defaultfilters import slugify

@receiver(post_save, sender=Blog)
def save_blog(sender, created, instance, **kwargs):
    if created:
        instance.slug = slugify(instance.name + str(instance.created_at))
        instance.save()