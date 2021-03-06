# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-05 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_auto_20170818_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='address',
            field=models.TextField(default='4270 W. 6th St.  Los Angeles,  California  90020'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='contact_title',
            field=models.TextField(default='Tyndale International University'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='emails',
            field=models.TextField(default='tiu4270@gmail.com / info.tyndaleinternationaluniversity@gmail.com'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='office_hours',
            field=wagtail.core.fields.RichTextField(default='Office Hours'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='phone_number',
            field=models.TextField(default='(213) 595-3181'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='website',
            field=models.TextField(default='www.tyndaleinternationaluniversity.org / www.yalamission.org'),
        ),
        migrations.AlterField(
            model_name='coursedetailpage',
            name='video_url',
            field=models.CharField(default='PMJFfMWgyZI', max_length=255),
        ),
    ]
