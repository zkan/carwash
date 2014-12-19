from django.db import IntegrityError
from django.test import TestCase

from ..models import Car
from members.models import Member


class CarTest(TestCase):
    def setUp(self):
        self.owner = Member.objects.create(
            first_name='Kan',
            last_name='Ouivirach'
        )

        self.car = Car()

    def test_add_new_car(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = 'Triton'
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = 'Bangkok'
        self.car.color = 'Brown'
        self.car.size = 'L'

        self.assertFalse(self.car.pk)

        self.car.save()

        self.assertTrue(self.car.pk)

        car = Car.objects.get(id=self.car.id)

        self.assertEqual(car.owner.first_name, self.owner.first_name)
        self.assertEqual(car.owner.last_name, self.owner.last_name)
        self.assertEqual(car.brand, 'Mitsubishi')
        self.assertEqual(car.model, 'Triton')
        self.assertEqual(car.license_plate_letters, '2AB')
        self.assertEqual(car.license_plate_numbers, '5334')
        self.assertEqual(car.license_plate_province, 'Bangkok')
        self.assertEqual(car.color, 'Brown')
        self.assertEqual(car.size, 'L')

    def test_add_new_car_without_owner_should_fail(self):
        with self.assertRaises(ValueError):
            self.car.owner = None

    def test_add_new_car_without_brand_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = None
        self.car.model = 'Triton'
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = 'Bangkok'
        self.car.color = 'Brown'
        self.car.size = 'L'

        self.assertRaises(IntegrityError, self.car.save)

    def test_add_new_car_without_model_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = None
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = 'Bangkok'
        self.car.color = 'Brown'
        self.car.size = 'L'

        self.assertRaises(IntegrityError, self.car.save)

    def test_add_new_car_without_license_plate_letters_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = 'Triton'
        self.car.license_plate_letters = None
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = 'Bangkok'
        self.car.color = 'Brown'
        self.car.size = 'L'

        self.assertRaises(IntegrityError, self.car.save)

    def test_add_new_car_without_license_plate_numbers_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = 'Triton'
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = None
        self.car.license_plate_province = 'Bangkok'
        self.car.color = 'Brown'
        self.car.size = 'L'

        self.assertRaises(IntegrityError, self.car.save)

    def test_add_new_car_without_license_plate_province_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = 'Triton'
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = None
        self.car.color = 'Brown'
        self.car.size = 'L'

        self.assertRaises(IntegrityError, self.car.save)

    def test_add_new_car_without_color_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = 'Triton'
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = 'Bangkok'
        self.car.color = None
        self.car.size = 'L'

        self.assertRaises(IntegrityError, self.car.save)

    def test_add_new_car_without_size_should_fail(self):
        self.car.owner = self.owner
        self.car.brand = 'Mitsubishi'
        self.car.model = 'Triton'
        self.car.license_plate_letters = '2AB'
        self.car.license_plate_numbers = '5334'
        self.car.license_plate_province = 'Bangkok'
        self.car.color = 'Brown'
        self.car.size = None

        self.assertRaises(IntegrityError, self.car.save)
