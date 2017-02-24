from django.shortcuts import render

# Create your views here.
def vendas_inicial(request):
    return render(request, 'vendasapp/vendas_inicial.html', {})

# Produtos 
def grupo_produtos(request):
    return render(request, 'vendasapp/grupo_produtos.html', {})

def cadastro_produtos(request):
    return render(request, 'vendasapp/cadastro_produtos.html', {})