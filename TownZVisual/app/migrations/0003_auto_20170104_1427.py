# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-01-04 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_playertown'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playertown',
            old_name='Rescources',
            new_name='Money',
        ),
    ]