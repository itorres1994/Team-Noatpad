# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-01 01:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('track_n_drive', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='user_ins',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='email',
            old_name='user_ins',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='insurance',
            old_name='user_ins',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='license',
            old_name='user_ins',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='notifications',
            old_name='user_ins',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='phone',
            old_name='user_ins',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='settings',
            old_name='user_ins',
            new_name='user',
        ),
    ]
