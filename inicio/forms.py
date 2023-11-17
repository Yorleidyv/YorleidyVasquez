from django import forms
from ckeditor.fields import RichTextField
from .models import Tratamiento

class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['nombre', 'descripcion', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'ckeditor'}),
        }
