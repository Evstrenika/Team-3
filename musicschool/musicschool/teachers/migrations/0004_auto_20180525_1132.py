# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-25 01:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20180521_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
