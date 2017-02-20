from django.contrib import admin

# Register your models here.
from .models import Produto, GrupoProduto
admin.site.register(Produto)
admin.site.register(GrupoProduto)