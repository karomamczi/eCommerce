# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170610_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='user',
        ),
    ]
