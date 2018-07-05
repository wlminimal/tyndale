# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-02 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0005_capitalizeverbose'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0026_auto_20170502_2123'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SemesterPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('semester_name', models.CharField(default='Choose Semester', max_length=100)),
                ('start_month', models.CharField(default='Mar', max_length=40)),
                ('start_date', models.CharField(default='27', max_length=40)),
                ('thumb_image', models.ForeignKey(help_text='500 x 500 image for semester index page ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='courseindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='courseindexpage',
            name='thumb_image',
        ),
        migrations.DeleteModel(
            name='CourseIndexPage',
        ),
    ]
