# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staffing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='probability',
            field=models.IntegerField(default=50, verbose_name='Proba'),
        ),
    ]
