# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoProduto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('data_inclusao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_alteracao', models.DateTimeField(null=True, blank=True)),
                ('usuario_alteracao', models.ForeignKey(blank=True, null=True, related_name='user_ua_gp_fk', to=settings.AUTH_USER_MODEL)),
                ('usuario_inclusao', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_ui_gp_fk')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('descricao', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('titulo_web', models.CharField(max_length=100)),
                ('valor_unitario', models.DecimalField(max_digits=12, decimal_places=2)),
                ('data_inclusao', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_alteracao', models.DateTimeField(null=True, blank=True)),
                ('id_grupo_produto', models.ForeignKey(to='vendasapp.GrupoProduto', related_name='grupoProduto_id_fk')),
                ('usuario_alteracao', models.ForeignKey(blank=True, null=True, related_name='user_ua_pr_fk', to=settings.AUTH_USER_MODEL)),
                ('usuario_inclusao', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='user_ui_pr_fk')),
            ],
        ),
    ]
