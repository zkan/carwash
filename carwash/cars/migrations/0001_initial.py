# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('brand', models.CharField(max_length=300)),
                ('model', models.CharField(max_length=300)),
                ('license_plate_letters', models.CharField(max_length=10)),
                ('license_plate_numbers', models.CharField(max_length=10)),
                ('license_plate_provice', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=5)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
