# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0005_auto_20180430_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='weather',
            field=models.CharField(default='Sunny', max_length=20, choices=[('Sunny', 'Sunny'), ('Windy', 'Windy'), ('Rainy', 'Rainy'), ('Snowy', 'Snowy'), ('Foggy', 'Foggy'), ('Cloudy', 'Cloudy'), ('Stormy', 'Stormy')]),
        ),
    ]
