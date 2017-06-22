# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-12 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20170210_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbackdetails',
            options={'verbose_name': 'detail', 'verbose_name_plural': 'Listado de feedbacks'},
        ),
        migrations.AlterField(
            model_name='feedbackdetails',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Leido'), (3, 'Sin atenci\xf3n'), (4, 'Respondido')], default=1, verbose_name='Status'),
        ),
    ]