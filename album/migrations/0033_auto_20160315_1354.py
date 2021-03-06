# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-15 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0032_auto_20160314_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='gaan',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='albumname',
            name='chobi',
            field=models.ManyToManyField(blank=True, null=True, to='album.Chobi', verbose_name='\u099b\u09ac\u09bf'),
        ),
        migrations.AlterField(
            model_name='albumname',
            name='prokashok',
            field=models.ManyToManyField(blank=True, null=True, to='album.Prokashok', verbose_name='\u09aa\u09cd\u09b0\u0995\u09be\u09b6\u0995'),
        ),
    ]
