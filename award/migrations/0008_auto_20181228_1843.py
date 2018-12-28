# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-28 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0007_auto_20181228_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='content',
            field=models.IntegerField(choices=[(4, '4'), (8, '8'), (10, '10'), (9, '9'), (6, '6'), (7, '7'), (1, '1'), (3, '3'), (5, '5'), (2, '2')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.IntegerField(choices=[(4, '4'), (8, '8'), (10, '10'), (9, '9'), (6, '6'), (7, '7'), (1, '1'), (3, '3'), (5, '5'), (2, '2')], default=0),
        ),
        migrations.AlterField(
            model_name='rating',
            name='usability',
            field=models.IntegerField(choices=[(4, '4'), (8, '8'), (10, '10'), (9, '9'), (6, '6'), (7, '7'), (1, '1'), (3, '3'), (5, '5'), (2, '2')], default=0),
        ),
    ]
