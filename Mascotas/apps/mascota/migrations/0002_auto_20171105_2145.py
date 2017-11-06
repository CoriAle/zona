# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacuna',
            name='fecha_vencimiento',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacuna',
            name='funcion',
            field=models.CharField(default='vitamina', max_length=100),
            preserve_default=False,
        ),
    ]