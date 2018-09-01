from django.test import TestCase

from users.models import User


class TestUser(TestCase):
    """Test class for users app."""

    def test_user_default_fields(self):
        """Test if the user is created with the default fields."""
        user = User.objects.create_user(
            username='test',
            password='test123',
            email='test@test.com',
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.user_type, 'M')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_authorized, False)

    def test_superuser_default_fields(self):
        """Test if the superuser is created with the default fields."""
        user = User.objects.create_superuser(
            username='test',
            password='test123',
            email='test@test.com',
        )

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.user_type, 'A')
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_authorized, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)
