# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-02 21:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0025_auto_20170502_1836'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SemesterPage',
            new_name='SemesterIndexPage',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='semester_thumb_image',
        ),
        migrations.AddField(
            model_name='coursedetailpage',
            name='course_description',
            field=wagtail.core.fields.RichTextField(default='Description of course'),
        ),
        migrations.AddField(
            model_name='coursedetailpage',
            name='course_name',
            field=models.TextField(default='Ancient Church History'),
        ),
        migrations.AddField(
            model_name='coursedetailpage',
            name='professor_name',
            field=models.CharField(default='Professor name', max_length=70),
        ),
        migrations.AddField(
            model_name='coursedetailpage',
            name='upload_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='coursedetailpage',
            name='video_url',
            field=models.URLField(default='http://www.youtube.com'),
        ),
        migrations.AddField(
            model_name='courseindexpage',
            name='semester_name',
            field=models.CharField(default='Choose Semester', max_length=100),
        ),
        migrations.AddField(
            model_name='courseindexpage',
            name='start_date',
            field=models.CharField(default='27', max_length=40),
        ),
        migrations.AddField(
            model_name='courseindexpage',
            name='start_month',
            field=models.CharField(default='Mar', max_length=40),
        ),
        migrations.AddField(
            model_name='courseindexpage',
            name='thumb_image',
            field=models.ForeignKey(help_text='550 x 550 image for semester index page ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
