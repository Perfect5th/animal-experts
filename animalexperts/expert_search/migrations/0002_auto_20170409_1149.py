# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldcategory',
            name='code',
            field=models.SlugField(unique=True),
        ),
    ]
