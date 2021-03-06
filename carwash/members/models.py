from django.db import models


class Member(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=300
    )

    email = models.EmailField(
        null=True,
        blank=True,
        max_length=254
    )

    birthdate = models.DateField(
        null=True,
        blank=True
    )

    phone = models.CharField(
        null=True,
        blank=True,
        max_length=20
    )

    signup_date = models.DateField(
        null=True,
        blank=True,
        auto_now_add=True
    )

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
