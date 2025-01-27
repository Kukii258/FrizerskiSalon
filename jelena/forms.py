from django import forms
from django.contrib import admin
from .models import Glavna_Frizura


class frizura_form(forms.ModelForm):
    class Meta:
        model = Glavna_Frizura
        fields = '__all__'
        widgets = {
            'opis': forms.Textarea(attrs={
                'rows': 5,  # Number of visible lines
                'cols': 60,  # Width of the textarea
                'style': 'resize: vertical;',  # Allow resizing only vertically
            }),
        }
