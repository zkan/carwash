# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_car_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='license_plate_provice',
            new_name='license_plate_province',
        ),
    ]
