import datetime

from django.db import IntegrityError
from django.test import TestCase

from ..models import Package


class PackageTest(TestCase):
    def setUp(self):
        self.package = Package()

    def test_add_new_package(self):
        self.package.name = 'Wash'
        self.package.created_date = '2015-05-04'
        self.package.start_date = '2015-06-11'
        self.package.notification_type = 'weekly'

        self.assertFalse(self.package.pk)

        self.package.save()

        self.assertTrue(self.package.pk)

        package = Package.objects.get(id=self.package.id)

        self.assertEqual(package.name, self.package.name)
        self.assertEqual(package.created_date, datetime.date(2015, 5, 4))
        self.assertEqual(package.start_date, datetime.date(2015, 6, 11))
        self.assertEqual(package.notification_type, 'weekly')

    def test_add_new_package_without_name_should_fail(self):
        self.package.name = None
        self.package.created_date = '2015-05-04'
        self.package.start_date = '2015-06-11'

        self.assertRaises(IntegrityError, self.package.save)

    def test_add_new_package_without_created_date_should_pass(self):
        self.package.name = 'Wash'
        self.package.created_date = None
        self.package.start_date = '2015-06-11'
        self.package.save()

        self.assertTrue(self.package.pk)

    def test_add_new_package_without_start_date_should_pass(self):
        self.package.name = 'Wash'
        self.package.created_date = '2015-05-04'
        self.package.start_date = None
        self.package.save()

        self.assertTrue(self.package.pk)

    def test_add_new_package_without_notification_type_should_fail(self):
        self.package.name = 'Wash'
        self.package.created_date = '2015-05-04'
        self.package.start_date = '2015-06-11'
        self.package.notification_type = None

        self.assertRaises(IntegrityError, self.package.save)
