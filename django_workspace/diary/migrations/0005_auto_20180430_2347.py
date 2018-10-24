# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20180430_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mood',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('HAPPY', 'Happy'), ('SAD', 'Sad'), ('EXCITED', 'Excited'), ('FURIOUS', 'Furious'), ('DEPRESSED', 'Depressed'), ('EXHAUSTED', 'Exhausted'), ('FRIGHTENED', 'Frightened'), ('RELAXED', 'Relaxed'), ('SURPRISED', 'Surprised'), ('ANGRY', 'Angry'), ('NERVOUS', 'Nervous'), ('LONELY', 'Lonely'), ('JEALOUS', 'Jealous'), ('SHY', 'Shy'), ('UPSET', 'Upset'), ('DISGUSTED', 'Disgusted')], max_length=123),
        ),
        migrations.AlterField(
            model_name='post',
            name='weather',
            field=models.CharField(default='SUNNY', max_length=20, choices=[('SUNNY', 'Sunny'), ('WINDY', 'Windy'), ('RAINY', 'Rainy'), ('SNOWY', 'Snowy'), ('FOGGY', 'Foggy'), ('CLOUDY', 'Cloudy'), ('STORMY', 'Stormy')]),
        ),
    ]
