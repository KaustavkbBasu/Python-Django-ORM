# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0004_auto_20180309_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.IntegerField(default=0),
        ),
    ]
