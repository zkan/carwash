import datetime
from datetime import date

from django.core.urlresolvers import reverse
from django.test import TestCase

from ..models import Member


class MemberAddViewTest(TestCase):
    def test_member_add_view_should_be_accesiable(self):
        response = self.client.get(reverse('member_add'))

        self.assertEqual(response.status_code, 200)

    def test_member_add_view_should_have_title(self):
        response = self.client.get(reverse('member_add'))

        expected = '<h1>New Member Information</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_member_add_view_should_have_member_form(self):
        response = self.client.get(reverse('member_add'))

        expected = '<form method="post">'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>First Name:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_first_name" maxlength="300" '
        expected += 'name="first_name" type="text" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Last Name:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_last_name" maxlength="300" '
        expected += 'name="last_name" type="text" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Email:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_email" name="email" type="email" />'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Birth Day:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<select id="id_birth_day" name="birth_day">'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Birth Month:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<select id="id_birth_month" name="birth_month">'
        self.assertContains(response, expected, status_code=200)

        expected = '<label>Birth Year:</label>'
        self.assertContains(response, expected, status_code=200)
        expected = '<select id="id_birth_year" name="birth_year">'
        self.assertContains(response, expected, status_code=200)

        expected = "<label>Phone:</label>"
        self.assertContains(response, expected, status_code=200)
        expected = '<input id="id_phone" maxlength="100" name="phone" '
        expected += 'type="text" />'
        self.assertContains(response, expected, status_code=200)

    def test_add_new_member_successfully(self):
        data = {
            'first_name': 'Kan',
            'last_name': 'Ouivirach',
            'email': 'zkan.cs@gmail.com',
            'birth_day': '1',
            'birth_month': '2',
            'birth_year': '2010',
            'phone': '1234567'
        }

        response = self.client.post(
            reverse('member_add'),
            data=data
        )

        member = Member.objects.get(first_name='Kan')

        self.assertEqual(member.first_name, 'Kan')
        self.assertEqual(member.last_name, 'Ouivirach')
        self.assertEqual(member.email, 'zkan.cs@gmail.com')
        self.assertEqual(member.birthdate, datetime.date(2010, 2, 1))
        self.assertEqual(member.phone, '1234567')
        self.assertEqual(member.signup_date, date.today())
