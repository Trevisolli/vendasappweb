#coding:utf-8
from django.shortcuts import render, redirect
from .models import GrupoProduto

# Create your views here.
def vendas_inicial(request):
    return render(request, 'vendasapp/vendas_inicial.html', {})

# Produtos 
def grupo_produtos(request):
    return render(request, 'vendasapp/grupo_produtos.html', {})

def cadastro_produtos(request):
    return render(request, 'vendasapp/cadastro_produtos.html', {})


# Gravação de Dados


 
def cadastra_grupo_produto(request):
    if request.method == 'POST':
        form = GrupoProdutoForm(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = UnidadeForm()
 
    return render(request,"vendasapp_inicial.html",{'form':form})    