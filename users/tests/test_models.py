from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve
from django.utils.translation import activate
from django.conf import settings
from django.db.utils import IntegrityError

from users.forms import CustomUserCreationForm
# Create your tests here.

class CustomUserCreateTests(TestCase):

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
        field_label = user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'Имя пользователя')

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


class CustomUserTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username='max',
            email='max@email.com',
            user_lang='en',
            password='testpass123'
        )

    def test_user_name_label(self):
        field_label = self.user._meta.get_field('username').verbose_name
        self.assertEquals(field_label,'Имя пользователя')

    def test_email_label(self):
        field_label = self.user._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')

    def test_owner_label(self):
        field_label = self.user._meta.get_field('user_lang').verbose_name
        self.assertEquals(field_label,'Язык')

    def test_username_max_length(self):
        max_length = self.user._meta.get_field('username').max_length
        self.assertEquals(max_length, 30)

    def test_user_lang_max_length(self):
        max_length = self.user._meta.get_field('user_lang').max_length
        self.assertEquals(max_length, 2)

    def test_uniqueness(self):
        User = get_user_model()
        with self.assertRaisesMessage(IntegrityError, 'duplicate key value violates unique constraint'):
            User.objects.create(username='maxim', email='max@email.com', password='testpass123')

    def test_get_absolute_url(self):
        #This will also fail if the urlconf is not defined.
        self.assertEquals(self.user.get_absolute_url(), f'/{settings.LANGUAGE_CODE}/accounts/{self.user.id}/')


class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
