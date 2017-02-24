# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0003_auto_20170223_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoproduto',
            name='ativo',
            field=models.CharField(max_length=1, default='S', choices=[('S', 'Sim'), ('N', 'Não')]),
        ),
    ]
