from django import forms
from django.contrib.auth import get_user_model
from django.forms import fields

from django.contrib.auth.password_validation import validate_password
# from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    
    password1 = forms.CharField(max_length=127, validators=(validate_password, ))
    password2 = forms.CharField(max_length=127, validators=(validate_password, ))
    
    class Meta:
        model = User
        fields = {
            'first_name',
            'last_name',
            'username',
            'password',
            'email',
            'gender',
            'bio',
            'image',
            
        }
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 != password2:
            raise forms.ValidationError('Passwords are not same !')
        
        return super().clean()