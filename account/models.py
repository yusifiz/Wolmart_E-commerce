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
        return "https://thumbs.dreamstime.com/z/default-avatar-profile-icon-vector-social-media-user-photo-183042379.jpg"