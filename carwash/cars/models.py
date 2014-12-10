from django.db import models


class Car(models.Model):
    brand = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    model = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    license_plate_letters = models.CharField(
        null=False,
        blank=False,
        max_length=10
    )

    license_plate_numbers = models.CharField(
        null=False,
        blank=False,
        max_length=10
    )

    license_plate_provice = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )

    color = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )

    size = models.CharField(
        null=False,
        blank=False,
        max_length=5
    )
