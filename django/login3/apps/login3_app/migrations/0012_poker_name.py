# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login3_app', '0011_remove_poker_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='poker',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
