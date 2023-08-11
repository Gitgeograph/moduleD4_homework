from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ("author", "title", "categoryType", 'text')
        widgets = {
            'author': forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
            }),
            'title': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter title'
            }),
            'categoryType': forms.Select(attrs={
            'class': 'form-control',
            }),
            'text': forms.Textarea(attrs={
            'class': 'form-control',
            }),
        }
