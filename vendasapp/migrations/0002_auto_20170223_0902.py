# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoproduto',
            name='ativo',
            field=models.CharField(max_length=1, default='S'),
        ),
        migrations.AlterField(
            model_name='grupoproduto',
            name='usuario_alteracao',
            field=models.ForeignKey(null=True, related_name='vendasapp_grupoproduto_modified_by', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grupoproduto',
            name='usuario_inclusao',
            field=models.ForeignKey(related_name='vendasapp_grupoproduto_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produto',
            name='usuario_alteracao',
            field=models.ForeignKey(null=True, related_name='vendasapp_produto_modified_by', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produto',
            name='usuario_inclusao',
            field=models.ForeignKey(related_name='vendasapp_produto_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor_unitario',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
