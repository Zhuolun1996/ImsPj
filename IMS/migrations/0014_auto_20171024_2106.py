# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-24 13:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMS', '0013_events'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='events',
            new_name='event',
        ),
        migrations.RenameModel(
            old_name='resources',
            new_name='resource',
        ),
    ]