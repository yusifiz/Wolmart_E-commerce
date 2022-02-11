from django import forms
from .models import Contact
from django.db.models import fields

class ContactForm(forms.ModelForm):
    
    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Email...'}
    ))
    
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Name...'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Your Message...'})
        }