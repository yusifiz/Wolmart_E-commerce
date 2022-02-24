from django import forms
from .models import Comment


class BlogCommentForm(forms.ModelForm):

    email = forms.EmailField(label='Email', max_length=100, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}
    ))

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'body': forms.Textarea(
                attrs={'class': 'form-control mb-5', 'placeholder': 'Write a Comment',}),
        }