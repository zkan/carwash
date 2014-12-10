import datetime
from datetime import date

from django.db import IntegrityError
from django.test import TestCase

from ..models import Member


class MemberTest(TestCase):
    def setUp(self):
        self.member = Member()

    def test_add_new_member(self):
        self.member.first_name = 'Kan'
        self.member.last_name = 'Ouivirach'
        self.member.email = 'zkan.cs@gmail.com'
        self.member.birthdate = '1984-05-04'
        self.member.phone = '083-749-5568'

        self.assertFalse(self.member.pk)

        self.member.save()

        self.assertTrue(self.member.pk)

        member = Member.objects.get(id=self.member.id)

        self.assertEqual(member.first_name, 'Kan')
        self.assertEqual(member.last_name, 'Ouivirach')
        self.assertEqual(member.email, 'zkan.cs@gmail.com')
        self.assertEqual(member.birthdate, datetime.date(1984, 5, 4))
        self.assertEqual(member.phone, '083-749-5568')
        self.assertEqual(member.signup_date, date.today())

    def test_add_new_member_without_first_name_should_fail(self):
        self.member.first_name = None
        self.member.last_name = 'Ouivirach'
        self.member.email = 'zkan.cs@gmail.com'

        self.assertRaises(IntegrityError, self.member.save)

    def test_add_new_member_without_last_name_should_fail(self):
        self.member.first_name = 'Kan'
        self.member.last_name = None
        self.member.email = 'zkan.cs@gmail.com'

        self.assertRaises(IntegrityError, self.member.save)

    def test_add_new_member_without_email_should_pass(self):
        self.member.first_name = 'Kan'
        self.member.last_name = 'Ouivirach'
        self.member.email = None
        self.member.save()

        self.assertTrue(self.member.pk)

    def test_add_new_member_without_birthdate_should_pass(self):
        self.member.first_name = 'Kan'
        self.member.last_name = 'Ouivirach'
        self.member.birthdate = None
        self.member.save()

        self.assertTrue(self.member.pk)

    def test_add_new_member_without_phone_should_pass(self):
        self.member.first_name = 'Kan'
        self.member.last_name = 'Ouivirach'
        self.member.phone = None
        self.member.save()

        self.assertTrue(self.member.pk)
