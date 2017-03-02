from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.vendas_inicial, name='vendas_inicial'),
	url(r'^criar_grupo_produtos', views.criar_grupo_produtos, name='criar_grupo_produtos'),
	url(r'^listar_produtos', views.listar_produtos, name='listar_produtos'),     
   # url(r'^listar_produtos', views.listar_produtos_ativos, name='listar_produtos_ativos'),
]