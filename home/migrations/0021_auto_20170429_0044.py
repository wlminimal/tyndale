# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 00:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0020_professor_spec'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(default='Name', max_length=100)),
                ('spec', wagtail.wagtailcore.fields.RichTextField(default='Spec of professor')),
                ('class_name', models.TextField(default='class name')),
                ('order_number', models.IntegerField(default=10)),
                ('profile_image', models.ForeignKey(help_text='360x360 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='professor',
            name='profile_image',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
    ]