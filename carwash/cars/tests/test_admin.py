from django.test import TestCase
from django.contrib.auth.models import User


class CarAdminTest(TestCase):
    def test_access_car_admin(self):
        User.objects.create_superuser(
            'admin',
            'admin@autowash.com',
            'autowash'
        )
        self.client.login(username='admin', password='autowash')

        response = self.client.get('/admin/cars/car/')

        self.assertEqual(response.status_code, 200)
