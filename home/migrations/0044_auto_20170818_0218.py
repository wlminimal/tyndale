# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0043_auto_20170818_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='banner_image',
        ),
        migrations.AddField(
            model_name='newspage',
            name='description',
            field=wagtail.core.fields.RichTextField(default='이곳에서 틴데일 신학교에 대한 새로운 소식을 읽으시길 바랍니다.'),
        ),
        migrations.AddField(
            model_name='newspage',
            name='greeting',
            field=models.TextField(default='틴데일 신학교 게시판에 오신걸 환영합니다.'),
        ),
    ]
