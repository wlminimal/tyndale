# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 00:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0029_auto_20170503_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='grid_subtitle',
            field=models.TextField(default='Description of grid item'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='grid_title',
            field=models.CharField(default='Academic Programs', max_length=100),
        ),
    ]