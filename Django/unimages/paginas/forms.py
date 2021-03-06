from django import forms
from bootstrap_modal_forms.forms import BSModalModelForm
from .models import *


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['banco', 'agencia', 'conta', 'pix']
        banco = forms.CharField()
        agencia = forms.CharField()
        conta = forms.CharField()
        pix = forms.CharField()


class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'descricao', 'valor', 'duracao', 'pix']
        nome = forms.CharField()
        descricao = forms.CharField()
        valor = forms.FloatField(min_value=0)
        duracao = forms.IntegerField(min_value=0)
        pix = forms.CharField()


class AssinanteForm(forms.ModelForm):
    class Meta:
        model = Assinante
        fields = ['plano']
        data_de_inicio = forms.DateField()
        data_final = forms.DateField()
        plano = forms.CharField()


class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = ['titulo', 'descricao', 'valor',
                  'categoria', 'resolucao', 'formato', 'arquivo']


class CategoriaImagemForm(forms.ModelForm):
    class Meta:
        model = Categoria_imagem
        fields = ['nome']


class FormatoImagemForm(forms.ModelForm):
    class Meta:
        model = Formato_imagem
        fields = ['nome']


class ImagemFavoritaForm(forms.ModelForm):
    class Meta:
        model = Imagem_favorita
        fields = []


class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['estabelecimento_de_ensino', 'data_final',
                  'comprovante_de_matricula', 'plano']
        widgets = {
            'data_final': forms.DateInput(attrs={'type': 'date'})
        }

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
