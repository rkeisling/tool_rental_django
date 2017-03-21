# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 15:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tool_name', models.CharField(max_length=50)),
                ('tool_descrip', models.TextField()),
                ('price', models.FloatField()),
                ('date_added', models.DateTimeField(default=datetime.datetime(2017, 3, 21, 15, 53, 30, 537942, tzinfo=utc))),
                ('date_rented', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]