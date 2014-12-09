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

        self.assertFalse(self.member.pk)

        self.member.save()

        self.assertTrue(self.member.pk)

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
