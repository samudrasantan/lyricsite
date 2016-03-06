# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20160209_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gitikar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='album',
            name='lirisists',
        ),
        migrations.RemoveField(
            model_name='album',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='song',
            name='lirisists',
        ),
        migrations.RemoveField(
            model_name='song',
            name='publisher',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Lirisist',
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]
