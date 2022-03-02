from django import forms
from .models import Checkout

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ('adress1', 'adress2', 'town', 'zip', 'phone',)
        widgets = {
            'adress1': forms.TextInput(
                attrs={'class': 'form-control form-control-md ', 'placeholder': 'House number and street name'}),
            'adress2': forms.TextInput(
                attrs={'class': 'form-control form-control-md ', 'placeholder': 'Apartment, suite, unit, etc. (optional)'}),
            'town': forms.TextInput(
                attrs={'class': 'form-control form-control-md', 'placeholder': 'Town/City'}),
            'zip': forms.TextInput(
                attrs={'class': 'form-control form-control-md', 'placeholder': 'ZIP code'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control form-control-md', 'placeholder': 'Phone Number'}),
            
        }