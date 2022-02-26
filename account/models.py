from django.db import models

from django.contrib.auth.models import AbstractUser
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):

    GENDER_CHOICES = (
        (True, 'Male'), 
        (False, 'Female')
    )
    email = models.EmailField(_('email address'), blank=True, unique=True)
    image = models.ImageField(upload_to='accounts/profile/', blank=True, null=True)
    bio = models.TextField('Bio', null=True, blank=True)
    gender = models.BooleanField('Gender', choices=GENDER_CHOICES, default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def profile_picture(self):
        if self.image:
            return self.image
        return "https://www.google.com/url?sa=i&url=https%3A%2F%2Fpixabay.com%2Fimages%2Fsearch%2Fuser%2F&psig=AOvVaw0eNZRySltp0Hsen_aSCFxk&ust=1646077471828000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPj7pMrSoPYCFQAAAAAdAAAAABAJ"