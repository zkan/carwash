import datetime
from datetime import date

from django.test import TestCase

from ..forms import MemberForm
from ..models import Member


class MemberFormTest(TestCase):
    def test_form_should_contain_defined_fields(self):
        expected_fields = [
            'first_name',
            'last_name',
            'email',
            'birth_day',
            'birth_month',
            'birth_year',
            'phone'
        ]

        form = MemberForm()

        for each in expected_fields:
            self.assertTrue(each in form.fields)

    def test_input_valid_data_to_form(self):
        valid_data = [
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'phone': '1234567'
            }
        ]

        for each in valid_data:
            form = MemberForm(data=each)

            self.assertTrue(form.is_valid())
            self.assertFalse(form.errors)

    def test_input_invalid_data_to_form(self):
        invalid_data = [
            {
                'first_name': '',
                'last_name': 'Ouivirach',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'phone': '1234567'
            },
            {
                'first_name': 'Kan',
                'last_name': '',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'phone': '1234567'
            },
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'email': '',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'phone': '1234567'
            },
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '',
                'birth_month': '2',
                'birth_year': '2010',
                'phone': '1234567'
            },
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '1',
                'birth_month': '',
                'birth_year': '2010',
                'phone': '1234567'
            },
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '',
                'phone': '1234567'
            },
            {
                'first_name': 'Kan',
                'last_name': 'Ouivirach',
                'email': 'zkan.cs@gmail.com',
                'birth_day': '1',
                'birth_month': '2',
                'birth_year': '2010',
                'phone': ''
            }
        ]

        for each in invalid_data:
            form = MemberForm(data=each)

            self.assertFalse(form.is_valid())
            self.assertTrue(form.errors)

    def test_save_form_successfully_should_store_data(self):
        data = {
            'first_name': 'Kan',
            'last_name': 'Ouivirach',
            'email': 'zkan.cs@gmail.com',
            'birth_day': '1',
            'birth_month': '2',
            'birth_year': '2010',
            'phone': '1234567'
        }

        form = MemberForm(data=data)
        form.is_valid()
        form.save()

        member = Member.objects.get(first_name='Kan')

        self.assertEqual(member.first_name, 'Kan')
        self.assertEqual(member.last_name, 'Ouivirach')
        self.assertEqual(member.email, 'zkan.cs@gmail.com')
        self.assertEqual(member.birthdate, datetime.date(2010, 2, 1))
        self.assertEqual(member.phone, '1234567')
        self.assertEqual(member.signup_date, date.today())
