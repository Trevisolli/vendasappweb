from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    url(r'^$', views.vendas_inicial, name='vendas_inicial'),
    url(r'^grupo_produtos', views.grupo_produtos, name='grupo_produtos'),
]