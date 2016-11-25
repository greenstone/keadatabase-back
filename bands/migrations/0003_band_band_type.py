# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-25 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0002_remove_bandcombo_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='band_type',
            field=models.CharField(choices=[('N', 'Letter (New)'), ('O', 'Colour (Old)'), ('M', 'Identifier (Metal)')], default='N', editable=False, max_length=1),
            preserve_default=False,
        ),
    ]
