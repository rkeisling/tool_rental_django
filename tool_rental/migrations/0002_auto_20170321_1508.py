# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 20:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tool_rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='num_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tool',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 21, 20, 8, 11, 969394, tzinfo=utc)),
        ),
    ]
