# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-05 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0036_auto_20190404_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='_image_list',
        ),
        migrations.RemoveField(
            model_name='video',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='video',
            name='host',
        ),
        migrations.RemoveField(
            model_name='video',
            name='rejected',
        ),
        migrations.RemoveField(
            model_name='video',
            name='source',
        ),
        migrations.RemoveField(
            model_name='video',
            name='verified',
        ),
    ]
