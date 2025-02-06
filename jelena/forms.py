from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError

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

#import pitcures from folder
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={'multiple': True}))  # Allow multiple file selection
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d) for d in data]
        return [single_file_clean(data)]


class FileFieldForm(forms.Form):
    file_field = MultipleFileField()



class SlikaForm(forms.ModelForm):
    class Meta:
        model = Glavna_Frizura
        fields = "__all__"

    def clean_upload(self):
        upload = self.cleaned_data.get("slika_frizura")
        if upload:
            ext = upload.name.split(".")[-1].lower()
            if ext not in ["jpg", "jpeg", "png"]:
                raise ValidationError("Slika mora biti u .JPG/.JPNG/.PNG formatu")
        return upload
