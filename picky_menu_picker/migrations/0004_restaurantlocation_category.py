# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picky_menu_picker', '0003_auto_20171014_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
