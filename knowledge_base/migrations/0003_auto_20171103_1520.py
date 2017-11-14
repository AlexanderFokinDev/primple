# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-03 12:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_base', '0002_auto_20170831_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='knowledgebase',
            name='change_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='knowledgebase',
            name='create_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='knowledgebase',
            name='short_description',
            field=models.TextField(default='short_name'),
            preserve_default=False,
        ),
    ]