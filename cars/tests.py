from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from django.utils.translation import activate
from django.contrib.auth import get_user_model

from .models import Car
# Create your tests here.


class HomepageTests(SimpleTestCase):

    def test_homepage_redirect_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_homepage_auth_redirect_status_code(self):
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, 302)


class CarTests(TestCase):


    def setUp(self):

        self.car = Car.objects.create(
            name='Toyota',
            year='2000',
        )

    def test_car_listing(self):
        self.assertEqual(f'{self.car.name}', 'Toyota')
        self.assertEqual(f'{self.car.year}', '2000')
