from django.db import models

# Create your models here.
from django.utils import timezone

class GrupoProduto(models.Model):
	descricao = models.CharField(max_length=100)
	usuario_inclusao = models.ForeignKey('auth.User', related_name='user_ui_gp_fk')
	data_inclusao = models.DateTimeField(default=timezone.now)
	usuario_alteracao = models.ForeignKey('auth.User', related_name='user_ua_gp_fk', null=True, blank=True)    
	data_alteracao = models.DateTimeField(null=True, blank=True)

class Produto(models.Model):
	descricao = models.CharField(max_length=100) 
	texto = models.TextField()
	titulo_web = models.CharField(max_length=100)
	id_grupo_produto = models.ForeignKey('GrupoProduto', related_name='grupoProduto_id_fk')
	valor_unitario = models.DecimalField(max_digits=12, decimal_places=2) 
	usuario_inclusao = models.ForeignKey('auth.User', related_name='user_ui_pr_fk')
	data_inclusao = models.DateTimeField(default=timezone.now)
	usuario_alteracao = models.ForeignKey('auth.User', related_name='user_ua_pr_fk', null=True, blank=True)    
	data_alteracao = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return self.titulo_web  