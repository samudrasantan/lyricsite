# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 08:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0006_auto_20160210_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gitikar',
            old_name='name',
            new_name='titel',
        ),
    ]
