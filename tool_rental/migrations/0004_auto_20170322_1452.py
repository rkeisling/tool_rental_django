# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tool_rental', '0003_auto_20170322_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 3, 22, 19, 52, 2, 413287, tzinfo=utc)),
        ),
    ]