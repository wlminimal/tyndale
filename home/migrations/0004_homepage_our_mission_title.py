# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-26 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170426_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='our_mission_title',
            field=models.TextField(default='Preparing students to serve Christ and his church through biblical, experiential, and practical ministry'),
        ),
    ]