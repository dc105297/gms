# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-04 20:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0004_auto_20170404_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert',
            options={'get_latest_by': 'alert_created'},
        ),
    ]