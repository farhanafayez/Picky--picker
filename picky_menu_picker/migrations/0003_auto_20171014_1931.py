# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-14 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picky_menu_picker', '0002_restaurants_location'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restaurants',
            new_name='RestaurantLocation',
        ),
    ]
