"""Forms for the CineAI blog app."""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = ['title', 'movie_title', 'content', 'rating', 'sentiment']
        widgets = {
            'title':       forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Review title'}),
            'movie_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Movie name'}),
            'content':     forms.Textarea(attrs={'class': 'form-control', 'rows': 6, 'placeholder': 'Write your review...'}),
            'rating':      forms.Select(attrs={'class': 'form-select'}),
            'sentiment':   forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'movie_title': 'Movie Title',
            'sentiment':   'Sentiment (or use AI Analyzer)',
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'your@email.com'
    }))

    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})
