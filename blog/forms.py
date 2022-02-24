from django import forms
from .models import Blog
from django.db.models import fields

class BlogCommentForm(forms.ModelForm):

    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}
    ))

    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'body': forms.Textarea(
                attrs={'cols':30,'rows':6,'id':'comment','class': 'form-control mb4', 'placeholder': 'Write a Comment'})
        }