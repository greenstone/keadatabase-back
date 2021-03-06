# Generated by Django 3.0.3 on 2020-04-15 12:28

import django.contrib.gis.db.models.fields
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0007_gridtile'),
    ]

    operations = [
        migrations.AddField(
            model_name='gridtile',
            name='centroid',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='gridtile',
            name='neighbours',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=7), blank=True, null=True, size=8),
        ),
    ]
