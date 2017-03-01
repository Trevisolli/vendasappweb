from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.vendas_inicial, name='vendas_inicial'),
    url(r'^novo_grupo_produtos', views.novo_grupo_produtos, name='novo_grupo_produtos'),
]