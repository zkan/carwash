from django.test import TestCase

from ..models import Member


class MemberTest(TestCase):
    def test_add_new_member(self):
        member = Member()
        member.first_name = 'Kan'
        member.last_name = 'Ouivirach'
        member.email = 'zkan.cs@gmail.com'

        self.assertFalse(member.pk)

        member.save()

        self.assertTrue(member.pk)
