from django import forms
from .models import Tweet


class PostForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = '__all__'
