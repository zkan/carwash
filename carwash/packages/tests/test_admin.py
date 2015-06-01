from django.test import TestCase
from django.contrib.auth.models import User


class PackageAdminTest(TestCase):
    def test_access_package_admin(self):
        User.objects.create_superuser(
            'admin',
            'admin@autowash.com',
            'autowash'
        )
        self.client.login(username='admin', password='autowash')

        response = self.client.get('/admin/packages/package/')

        self.assertEqual(response.status_code, 200)
