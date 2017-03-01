# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0004_auto_20170224_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoproduto',
            name='ativo',
            field=models.CharField(default='S', choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='grupoproduto',
            name='descricao',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Descrição do Grupo'),
        ),
        migrations.AlterField(
            model_name='grupoproduto',
            name='texto',
            field=models.TextField(verbose_name='Texto detalhando o grupo.'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
