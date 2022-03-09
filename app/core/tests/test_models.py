from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating the new user with email succesesful"""
        email = "foranytests.me@gmail.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalaized(self):
        """Test the email for a new user is normalized"""
        email = "FORANYTEST.me@gmail.com"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())
