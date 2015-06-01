from django.db import models


class Package(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    created_date = models.DateField(
        null=True,
        blank=True
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )
