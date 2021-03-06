# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0008_auto_20170428_0436'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicspage',
            name='main_description',
            field=wagtail.core.fields.RichTextField(default='Description'),
        ),
        migrations.AddField(
            model_name='academicspage',
            name='main_image',
            field=models.ForeignKey(help_text='1500x1000 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='academicspage',
            name='main_title',
            field=models.TextField(default='About Tyndale International University'),
        ),
    ]
