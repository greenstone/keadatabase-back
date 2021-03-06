# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('birds', '0001_initial'),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandCombo',
            fields=[
                ('bird', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='birds.Bird')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date_deployed', models.DateField()),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_imported', models.DateTimeField(blank=True, null=True)),
                ('study_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.StudyArea')),
            ],
            options={
                'ordering': ['bird'],
            },
        ),
    ]
