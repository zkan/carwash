# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='signup_date',
            field=models.DateField(auto_now_add=True, null=True),
            preserve_default=True,
        ),
    ]
