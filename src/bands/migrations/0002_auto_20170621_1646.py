# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bandcombo',
            name='bird',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='band_combo', serialize=False, to='birds.Bird'),
        ),
    ]
