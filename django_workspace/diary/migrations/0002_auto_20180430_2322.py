# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mood',
            field=models.CharField(default='HA', max_length=30, choices=[('HA', 'Happy'), ('SA', 'Sad'), ('EXC', 'Excited'), ('FU', 'Furious'), ('DE', 'Depressed'), ('EXH', 'Exhausted'), ('FR', 'Frightened'), ('RE', 'Relaxed'), ('SU', 'Surprised'), ('AN', 'Angry'), ('NE', 'Nervous'), ('LO', 'Lonely'), ('JE', 'Jealous'), ('SH', 'Shy'), ('UP', 'Upset'), ('DI', 'Disgusted')]),
        ),
        migrations.AddField(
            model_name='post',
            name='weather',
            field=models.CharField(default='SU', max_length=20, choices=[('SU', 'Sunny'), ('WI', 'Windy'), ('RA', 'Rainy'), ('SN', 'Snowy'), ('FO', 'Foggy'), ('CL', 'Cloudy'), ('ST', 'Stormy')]),
        ),
    ]
