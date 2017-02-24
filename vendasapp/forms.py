#coding:utf-8
from django import forms 
from .models import GrupoProduto
 
class GrupoProdutoForm(forms.ModelForm):
    class Meta:
        model = GrupoProduto
        fields = ['descricao','texto', 'ativo']