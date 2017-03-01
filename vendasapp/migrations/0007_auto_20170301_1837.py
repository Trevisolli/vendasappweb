# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0006_auto_20170301_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='id_grupo_produto',
            field=models.OneToOneField(related_name='grupo_produto_fk', to='vendasapp.GrupoProduto', default=''),
            preserve_default=False,
        ),
    ]
