# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 00:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20170428_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='spec',
            field=wagtail.wagtailcore.fields.RichTextField(default='Spec of professor'),
        ),
    ]
