# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-28 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0007_auto_20190228_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasktracking',
            name='in_date',
            field=models.DateTimeField(),
        ),
    ]
