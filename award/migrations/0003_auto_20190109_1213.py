# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-09 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_auto_20190109_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(choices=[(6, '6'), (7, '7'), (9, '9'), (2, '2'), (8, '8'), (4, '4'), (5, '5'), (1, '1'), (3, '3'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(choices=[(6, '6'), (7, '7'), (9, '9'), (2, '2'), (8, '8'), (4, '4'), (5, '5'), (1, '1'), (3, '3'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(choices=[(6, '6'), (7, '7'), (9, '9'), (2, '2'), (8, '8'), (4, '4'), (5, '5'), (1, '1'), (3, '3'), (10, '10')], default=0),
        ),
    ]