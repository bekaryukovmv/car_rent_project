from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils.translation import activate
from django.contrib.auth import get_user_model

from cars.models import Car
# Create your tests here.


class RedirectHomepageTests(TestCase):

    def test_homepage_no_lang_redirect_status_code(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)

    def test_homepage_no_auth_redirect_status_code(self):
        resp = self.client.get('/ru/')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, '/accounts/login/?next=/ru/', target_status_code=302)

class CarsListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_cars = 8
        for car_num in range(number_of_cars):
            Car.objects.create(name='Toyota %s' % car_num, year = '20%s' % car_num,)

    def setUp(self):
        User = get_user_model()
        test_user = User.objects.create_user(username='testuser', email='user@test.ru', password='testpass12345') 
        test_user.save()
        self.client.login(username='user@test.ru', password='testpass12345')

    def test_view_url_exists_at_desired_location(self):
        activate('en')
        resp = self.client.get('/en/')
        self.assertEqual(str(resp.context['user']), 'testuser')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        activate('ru')
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'home.html')
        self.assertContains(resp, 'Здравствуйте')

    def test_pagination_is_five(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('cars' in resp.context)
        self.assertTrue(resp.context['cars'])
        self.assertTrue( len(resp.context['cars']) == 5)

    def test_lists_all_cars(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('home')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('cars' in resp.context)
        self.assertTrue(resp.context['cars'])
        self.assertTrue( len(resp.context['cars']) == 3)


class TestCarCreateView(TestCase):

    def test_redirect_unlogin_users(self):
        resp = self.client.get('/ru/create_car/')
        self.assertEqual(resp.status_code, 302)

    def test_test_func(self):
        User = get_user_model()
        test_user = User.objects.create_user(username='testuser', email='user@test.ru', password='testpass12345') 
        test_user.save()
        self.client.login(username='user@test.ru', password='testpass12345')

        resp = self.client.get(reverse('create_car'))
        self.assertEqual(resp.status_code, 403)

    def test_templates_urls_statuscodes_create_car(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='testpass123'
        )
        activate('ru')
        self.client.login(username='admin@email.com', password='testpass123')
        resp = self.client.get('/ru/create_car/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'create_car.html')
        self.assertContains(resp, 'Добавить машину в базу')

    def test_eng_templates_reverse_urls_statuscodes_create_car(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@email.com',
            password='testpass123'
        )
        activate('en')
        self.client.login(username='admin@email.com', password='testpass123')
        resp = self.client.get(reverse('create_car'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'create_car.html')
        self.assertContains(resp, 'Add Car in a Base')
