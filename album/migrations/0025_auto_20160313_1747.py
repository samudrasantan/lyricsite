# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0024_auto_20160310_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chobi',
            options={'verbose_name': '\u099b\u09ac\u09bf', 'verbose_name_plural': '\u099b\u09ac\u09bf'},
        ),
        migrations.AlterModelOptions(
            name='gitikar',
            options={'verbose_name': '\u0997\u09c0\u09a4\u09bf\u0995\u09be\u09b0', 'verbose_name_plural': '\u0997\u09c0\u09a4\u09bf\u0995\u09be\u09b0'},
        ),
        migrations.AddField(
            model_name='chobi',
            name='caption',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='\u0995\u09cd\u09af\u09be\u09aa\u09b6\u09a8'),
        ),
    ]
