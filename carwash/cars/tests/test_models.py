from django.db import IntegrityError
from django.test import TestCase

from ..models import Car


class CarTest(TestCase):
    def test_add_new_car(self):
        car = Car()
        car.brand = 'Mitsubishi'
        car.model = 'Triton'
        car.license_plate_letters = '2AB'
        car.license_plate_numbers = '5334'
        car.license_plate_province = 'Bangkok'
        car.color = 'Brown'
        car.size = 'L'

        self.assertFalse(car.pk)

        car.save()

        self.assertTrue(car.pk)
