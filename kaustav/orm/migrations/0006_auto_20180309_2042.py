# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-09 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm', '0005_auto_20180309_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acc', to='orm.Account_Risk'),
        ),
    ]
