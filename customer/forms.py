# forms.py
from django import forms
from .models import uploadimage

class uploadimageForm(forms.ModelForm):
    class Meta:
        model = uploadimage
        fields = ['image']  # Include other fields as needed
