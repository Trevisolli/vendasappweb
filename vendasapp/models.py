from django.db import models

# Create your models here.
from django.utils import timezone

class Identificacao(models.Model):
    # Classe abstrata: Dados em comum na Classe, porém, no BD as informações são geradas
    #                  em todas as tabelas que herdam esta.
	class Meta:
		abstract = True

	usuario_inclusao = models.ForeignKey('auth.User', related_name='%(app_label)s_%(class)s_created_by')
	data_inclusao = models.DateTimeField(default=timezone.now)
	usuario_alteracao = models.ForeignKey('auth.User', related_name='%(app_label)s_%(class)s_modified_by', null=True, blank=True)
	data_alteracao = models.DateTimeField(null=True, blank=True)

class GrupoProduto(Identificacao):
	descricao = models.CharField(max_length=100)
	texto = models.TextField()
	ativo = models.CharField(max_length=1, default="S")

class Produto(Identificacao):
	descricao = models.CharField(max_length=100) 
	texto = models.TextField()
	titulo_web = models.CharField(max_length=100)
	id_grupo_produto = models.ForeignKey('GrupoProduto', related_name='grupoProduto_id_fk', null=True)
	valor_unitario = models.DecimalField(max_digits=15, decimal_places=2)