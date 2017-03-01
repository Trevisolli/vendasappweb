# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0005_auto_20170301_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoproduto',
            name='texto',
            field=models.TextField(verbose_name='Texto detalhando o grupo.', help_text='Texto para WEB'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(max_length=100, db_index=True, verbose_name='Descrição do Produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='id_grupo_produto',
            field=models.ForeignKey(related_name='grupoProduto_id_fk', null=True, verbose_name='Grupo do Produto', to='vendasapp.GrupoProduto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='texto',
            field=models.TextField(verbose_name='Texto exibido na WEB'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='titulo_web',
            field=models.CharField(max_length=100, verbose_name='Título WEB'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, verbose_name='Valor Unitário', max_digits=15),
        ),
    ]
