# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-11-14 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Play',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='生成时间')),
                ('finished_time', models.DateTimeField(auto_now=True, null=True, verbose_name='完成时间')),
            ],
        ),
    ]
