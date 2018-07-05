# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-28 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0017_auto_20170428_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Name', max_length=100)),
                ('class_name', models.CharField(default='class name', max_length=100)),
                ('order_number', models.IntegerField(default=10)),
                ('profile_image', models.ForeignKey(help_text='360x360 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.AddField(
            model_name='academicprogramdetailpage',
            name='academic_description',
            field=wagtail.core.fields.RichTextField(default='Academic Program Description'),
        ),
        migrations.AddField(
            model_name='academicprogramdetailpage',
            name='academic_image',
            field=models.ForeignKey(help_text='1500x1000 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='academicprogramdetailpage',
            name='academic_name',
            field=models.TextField(default='Academic Program Name'),
        ),
        migrations.AddField(
            model_name='academicprogramdetailpage',
            name='duration',
            field=models.CharField(default='8 weeks', max_length=50),
        ),
        migrations.AddField(
            model_name='academicprogramdetailpage',
            name='start_date',
            field=models.CharField(default='March 11, 2017', max_length=100),
        ),
    ]
