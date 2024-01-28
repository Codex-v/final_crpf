from django import forms
from .models import imageView


class imageform(forms.ModelForm):
    class Meta:
        model = imageView
        fields = ['name','image']