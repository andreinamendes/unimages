from django import forms
from .models import *


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['banco', 'agencia', 'conta', 'pix']
        banco = forms.CharField()
        agencia = forms.CharField()
        conta = forms.CharField()
        pix = forms.CharField()
