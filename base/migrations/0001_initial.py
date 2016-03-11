# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('birthday', models.DateField()),
                ('student_ticket', models.IntegerField()),
                ('slug', models.SlugField()),
                ('student_group', models.ForeignKey(to='base.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='praepostor',
            field=models.ForeignKey(blank=True, to='base.Student', null=True),
        ),
    ]
