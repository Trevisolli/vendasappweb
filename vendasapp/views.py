#coding:utf-8
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import GrupoProduto

# Create your views here.
def vendas_inicial(request):
    return render(request, 'vendasapp/vendas_inicial.html', {})

# Produtos 
def novo_grupo_produtos(request):
    return render(request, 'vendasapp/novo_grupo_produtos.html', {})

def cadastro_produtos(request):
    return render(request, 'vendasapp/cadastro_produtos.html', {})

