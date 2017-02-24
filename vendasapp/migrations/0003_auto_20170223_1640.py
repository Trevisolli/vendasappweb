# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0002_auto_20170223_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupoproduto',
            name='texto',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='produto',
            name='id_grupo_produto',
            field=models.ForeignKey(related_name='grupoProduto_id_fk', to='vendasapp.GrupoProduto', null=True),
        ),
    ]
