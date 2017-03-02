#coding:utf-8
from django.shortcuts import render, redirect
from .models import Produto

# Create your views here.
def vendas_inicial(request):
    return render(request, 'vendasapp/vendas_inicial.html', {})

# Produtos 
def criar_grupo_produtos(request):
    return render(request, 'vendasapp/criar_grupo_produtos.html', {})

def listar_produtos(request):
    produtos = Produto.objects.all().filter(ativo__contains="S")
    context = {
        'produtos': produtos,
    }
    return render(request, 'vendasapp/listar_produtos.html', context)    

def cadastro_produtos(request):
    return render(request, 'vendasapp/cadastro_produtos.html', {})

