# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-16 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Authors', to='books_authors_app.Book'),
        ),
    ]
