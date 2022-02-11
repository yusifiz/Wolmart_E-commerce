from django.db import models

# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    
    
    def __str__(self):
        return self.email
    
    class Meta():
        verbose_name = 'Contact messages'
        verbose_name_plural = 'Contact messages'