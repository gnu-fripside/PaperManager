# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 01:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=64)),
                ('paperHashCode', models.CharField(max_length=64)),
                ('content', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='PaperNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=512)),
                ('publishTime', models.DateTimeField()),
                ('addTime', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=1024)),
                ('source', models.CharField(max_length=256)),
                ('filePath', models.CharField(max_length=256)),
                ('hashCode', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TagTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('userId', models.CharField(max_length=64)),
                ('father', models.CharField(max_length=64)),
            ],
        ),
    ]
