# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-04 20:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0003_alert_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert',
            options={'get_latest_by': 'creation_date'},
        ),
    ]