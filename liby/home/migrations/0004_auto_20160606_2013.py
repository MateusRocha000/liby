# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 23:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160606_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troca',
            name='avaliacao_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='troca',
            name='avaliacao_2',
            field=models.TextField(blank=True),
        ),
    ]
