# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-16 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0036_gaan_surokar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albumname',
            name='album_text',
            field=models.CharField(blank=True, max_length=10000, null=True, verbose_name='\u09ac\u09bf\u09ac\u09b0\u09a8'),
        ),
    ]
