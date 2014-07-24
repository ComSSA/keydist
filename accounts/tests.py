from django.test import TestCase
from django.utils import unittest
from accounts.models import KeydistUser, KeydistUserManager
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

# Create your tests here.
class AccountTestCase(TestCase):
    u1_sn = '16927140'
    u1_first_name = "User"
    u1_last_name = "One"
    u1_password = 'PasswordForUser1'

    u2_sn = '555555J'
    u2_first_name = "User"
    u2_last_name = "Two"
    u2_password = 'PasswordForUser2'

    def setUp(self):
        self.u1 = KeydistUser.objects.create_user(
            curtin_id = self.u1_sn,
            first_name = self.u1_first_name,
            last_name = self.u1_last_name,
            password = self.u1_password
        )
        self.u1.save()

        self.u2 = KeydistUser.objects.create_superuser(
            curtin_id = self.u2_sn,
            first_name = self.u2_first_name,
            last_name = self.u2_last_name,
            password = self.u2_password
        )
        self.u2.save()

    def test_curtin_status_student(self):
        self.assertEqual(self.u1.curtin_status, KeydistUser.STUDENT)

    def test_curtin_status_staff(self):
        self.assertEqual(self.u2.curtin_status, KeydistUser.STAFFASSOC)

    def test_email_student(self):
        self.assertEqual(self.u1.email, '16927140@student.curtin.edu.au')

    def test_email_staff(self):
        self.assertEqual(self.u2.email, '555555J@curtin.edu.au')

    def test_auth_with_correct_credetials(self):
        self.assertEqual(authenticate(curtin_id = self.u1_sn, password = self.u1_password), self.u1)

    def test_auth_with_incorrect_credentials(self):
        self.assertEqual(authenticate(curtin_id = self.u1_sn, password = self.u1_password + '1'), None)

    def test_superuser_auth_with_correct_credetials(self):
        self.assertEqual(authenticate(curtin_id = self.u2_sn, password = self.u2_password), self.u2)

    def test_superuser_auth_with_incorrect_credentials(self):
        self.assertEqual(authenticate(curtin_id = self.u1_sn, password = self.u2_password + '1'), None)

    def test_full_name(self):
        self.assertEqual(self.u1.full_name, "User One")
        self.assertEqual(self.u2.full_name, "User Two")

    def test_short_name(self):
        self.assertEqual(self.u1.short_name, "User O")
        self.assertEqual(self.u2.short_name, "User T")

    def test_unicode(self):
        self.assertEqual(self.u1.__unicode__(), "User One")
        self.assertEqual(self.u2.__unicode__(), "User Two")