# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login3_app', '0009_auto_20170628_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='poker',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
