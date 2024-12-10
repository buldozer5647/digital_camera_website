from django import forms

from .models import DigitalImage

class DigitalImageForm(forms.ModelForm):
    class Meta:
        model = DigitalImage
        fields = ["title", "description", "image", "alt_text"]