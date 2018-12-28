# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0014_auto_20181228_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(choices=[(3, '3'), (6, '6'), (2, '2'), (1, '1'), (4, '4'), (8, '8'), (7, '7'), (5, '5'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(choices=[(3, '3'), (6, '6'), (2, '2'), (1, '1'), (4, '4'), (8, '8'), (7, '7'), (5, '5'), (9, '9'), (10, '10')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(choices=[(3, '3'), (6, '6'), (2, '2'), (1, '1'), (4, '4'), (8, '8'), (7, '7'), (5, '5'), (9, '9'), (10, '10')], default=0),
        ),
    ]
