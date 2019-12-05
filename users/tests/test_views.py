from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model

from users.views import UserDetail, UserUpdate, UserDelete

# Create your tests here.
class UserProfilePageTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.test_user = User.objects.create_user(username='testuser', email='user@test.ru', password='testpass12345') 
        self.test_user.save()
        self.client.login(username='user@test.ru', password='testpass12345')
        url = reverse('users:dashboard', kwargs={'pk': self.test_user.id})
        self.response = self.client.get(url)

    def test_accounts_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_accounts_template(self):
        self.assertTemplateUsed(self.response, 'dashboard.html')

    def test_accounts_contains_correct_html(self):
        self.assertContains(self.response, 'Профиль пользователя')

    def test_accounts_does_not_contain_incorrect_html(self):
        self.assertNotContains( self.response, 'Hi there! I should not be on the page.')

    def test_accounts_url_resolves_UserDetailview(self):
        view = resolve(f'/ru/accounts/{self.test_user.id}/')
        self.assertEqual(view.func.__name__, UserDetail.as_view().__name__)


class UserUpdatePageTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.test_user = User.objects.create_user(username='testuser', email='user@test.ru', password='testpass12345') 
        self.test_user.save()
        self.client.login(username='user@test.ru', password='testpass12345')
        url = reverse('users:user_edit', kwargs={'pk': self.test_user.id})
        self.response = self.client.get(url)

    def test_account_update_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_account_update_template(self):
        self.assertTemplateUsed(self.response, 'user_edit.html')

    def test_account_update_contains_correct_html(self):
        self.assertContains(self.response, 'Редактировать профиль')

    def test_account_update_does_not_contain_incorrect_html(self):
        self.assertNotContains( self.response, 'Hi there! I should not be on the page.')

    def test_account_update_url_resolves_UserUpdateview(self):
        view = resolve(f'/ru/accounts/{self.test_user.id}/edit/')
        self.assertEqual(view.func.__name__, UserUpdate.as_view().__name__)


class UserDeletePageTests(TestCase):

    def setUp(self):
        User = get_user_model()
        self.test_user = User.objects.create_user(username='testuser', email='user@test.ru', password='testpass12345') 
        self.test_user.save()
        self.client.login(username='user@test.ru', password='testpass12345')
        url = reverse('users:user_delete', kwargs={'pk': self.test_user.id})
        self.response = self.client.get(url)

    def test_account_delete_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_account_delete_template(self):
        self.assertTemplateUsed(self.response, 'delete_user.html')

    def test_account_delete_contains_correct_html(self):
        self.assertContains(self.response, 'Вы уверены, что хотите удалить свою страницу?')

    def test_account_delete_does_not_contain_incorrect_html(self):
        self.assertNotContains( self.response, 'Hi there! I should not be on the page.')

    def test_account_delete_url_resolves_UserDeleteview(self):
        view = resolve(f'/ru/accounts/{self.test_user.id}/delete/')
        self.assertEqual(view.func.__name__, UserDelete.as_view().__name__)
