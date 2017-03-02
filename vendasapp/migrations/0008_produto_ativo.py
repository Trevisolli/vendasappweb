# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendasapp', '0007_auto_20170301_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='ativo',
            field=models.CharField(max_length=1, default='S', choices=[('S', 'Sim'), ('N', 'Não')], verbose_name='Ativo?'),
        ),
    ]
