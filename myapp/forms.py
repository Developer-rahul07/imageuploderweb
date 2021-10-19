from django import forms
from .models import ImageUploder

class ImageForm(forms.ModelForm):
    class Meta:
        model  = ImageUploder
        fields = '__all__'