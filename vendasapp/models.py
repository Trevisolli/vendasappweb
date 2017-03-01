#coding:utf-8
from django.db import models

# Create your models here.
from django.utils import timezone

OPCOES_ATIVO = (
    ('S', 'Sim'),
    ('N', 'Não'),    
)

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
	descricao = models.CharField(db_index=True, max_length=100, verbose_name="Descrição do Grupo")
	texto = models.TextField(verbose_name="Texto detalhando o grupo.", help_text="Texto para WEB")
	ativo = models.CharField(max_length=1, choices=OPCOES_ATIVO, default="S", verbose_name="Ativo?")

	def __str__(self):	
		return self.descricao

class Produto(Identificacao):
	descricao = models.CharField(db_index=True, max_length=100,verbose_name="Descrição do Produto") 
	texto = models.TextField(verbose_name="Texto exibido na WEB")
	titulo_web = models.CharField(max_length=100, verbose_name="Título WEB")
	#id_grupo_produto = models.ForeignKey('GrupoProduto', related_name='grupoProduto_id_fk', null=True, verbose_name="Grupo do Produto")
	id_grupo_produto = models.OneToOneField("GrupoProduto", related_name="grupo_produto_fk")
	valor_unitario = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Valor Unitário")

	def __str__(self):	
		return self.descricao	