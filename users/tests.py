from django.contrib.auth import get_user_model
from django.test import TestCase
# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='max',
            email='max@email.com',
            user_lang='en',
            password='testpass123'
        )
        self.assertEqual(user.username, 'max')
        self.assertEqual(user.email, 'max@email.com')
        self.assertEqual(user.user_lang, 'en')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'admin')
        self.assertEqual(admin_user.email, 'admin@email.com')
        self.assertEqual(admin_user.user_lang, 'ru')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
