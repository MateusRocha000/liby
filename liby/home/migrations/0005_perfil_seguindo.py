# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-08 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20160606_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='seguindo',
            field=models.ManyToManyField(related_name='_perfil_seguindo_+', to='home.Perfil'),
        ),
    ]