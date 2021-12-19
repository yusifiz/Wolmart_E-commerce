from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.db import models
from django.forms import fields
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegistrationForm(UserCreationForm):
    
    
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control','placeholder':'New password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control','placeholder':'Confirm password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = (
            'first_name', 
            'last_name',
            'username',
            'email',
            'bio',
            'gender',
            'image',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'bio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bio'}),
        }

        # def clean(self):
        #     password1 = self.cleaned_data.get('password1') 
        #     password2 = self.cleaned_data.get('password2')

        #     if password1 != password2:
        #         raise forms.ValidationError('Paswwords are not same')
            
        #     return super().clean()
        
        
class LoginForm(forms.Form):
    email = forms.EmailField(max_length=127, widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'E-mail'}))
    password = forms.CharField(max_length=127, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder': 'Password'}))