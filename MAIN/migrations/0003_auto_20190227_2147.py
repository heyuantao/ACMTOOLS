# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-27 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_auto_20190227_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiaccountanalyzerecord',
            name='account_id',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='multiipanalyze',
            name='account_id',
            field=models.CharField(max_length=48),
        ),
    ]
