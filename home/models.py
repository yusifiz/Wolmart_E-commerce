from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(max_length=150,blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.email:
            return str(self.email)
        return str(self.id)
    
    
class HomeSlider(models.Model):
    image = models.ImageField(upload_to='home/slider/')
    thumbnail = models.ImageField(upload_to='home/thumbnail/')
    title = models.CharField(max_length=200, null=True,blank=True)
    desc = models.CharField(max_length=200,null=True, blank=True) 
    
    
