# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0004_auto_20180525_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='teacher',
            field=models.CharField(max_length=50),
        ),
    ]
