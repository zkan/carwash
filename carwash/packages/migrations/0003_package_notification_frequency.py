# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0002_package_notification_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='notification_frequency',
            field=models.IntegerField(default=1),
        ),
    ]
