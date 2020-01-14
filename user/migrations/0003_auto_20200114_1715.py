# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-14 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=8, verbose_name='性别'),
        ),
    ]
