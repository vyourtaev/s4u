# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-18 20:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170818_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='destination',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='destination', to='api.Account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='name',
            field=models.CharField(blank=True, choices=[(0, 'DEPOSIT'), (1, 'WITHDRAWAL'), (2, 'TRANSFER')], max_length=10, null=True),
        ),
    ]
