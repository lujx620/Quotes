# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-03 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20170503_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='log_reg.Users'),
        ),
    ]
