from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from members.models import Member


class Car(models.Model):
    owner = models.ForeignKey(
        Member,
        null=False,
        blank=False,
        verbose_name=_('owner'),
        default=0
    )

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

    license_plate_province = models.CharField(
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

    def __unicode__(self):
        return '%s %s (%s %s)' % (
            self.brand,
            self.model,
            self.owner.first_name,
            self.owner.last_name
        )
