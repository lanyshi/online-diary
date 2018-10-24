# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20180430_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='mood',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('HA', 'Happy'), ('SA', 'Sad'), ('EXC', 'Excited'), ('FU', 'Furious'), ('DE', 'Depressed'), ('EXH', 'Exhausted'), ('FR', 'Frightened'), ('RE', 'Relaxed'), ('SU', 'Surprised'), ('AN', 'Angry'), ('NE', 'Nervous'), ('LO', 'Lonely'), ('JE', 'Jealous'), ('SH', 'Shy'), ('UP', 'Upset'), ('DI', 'Disgusted')], max_length=49),
        ),
    ]
