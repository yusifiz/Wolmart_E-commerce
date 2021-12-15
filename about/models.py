from django.db import models

# Create your models here.

class Leaders(models.Model):
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    name = models.CharField(max_length=127, verbose_name='Name', null=True, blank=True)
    specialty = models.CharField(max_length=127, verbose_name='Speciality', null=True, blank=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'
        ordering = ('created_at',)

    
    def __str__(self):
        return self.name