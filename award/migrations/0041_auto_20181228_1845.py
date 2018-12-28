# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0040_auto_20181228_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(choices=[(6, '6'), (7, '7'), (1, '1'), (9, '9'), (4, '4'), (10, '10'), (3, '3'), (2, '2'), (5, '5'), (8, '8')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(choices=[(6, '6'), (7, '7'), (1, '1'), (9, '9'), (4, '4'), (10, '10'), (3, '3'), (2, '2'), (5, '5'), (8, '8')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(choices=[(6, '6'), (7, '7'), (1, '1'), (9, '9'), (4, '4'), (10, '10'), (3, '3'), (2, '2'), (5, '5'), (8, '8')], default=0),
        ),
    ]
