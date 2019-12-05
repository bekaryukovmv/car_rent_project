from django.test import TestCase
from django.contrib.auth import get_user_model

from cars.models import Car

# Create your tests here.
class CarModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        Car.objects.create(
            name='Тойота',
            name_en = 'Toyota',
            year='2000',
        )

        Car.objects.create(
            name='Нива',
            year='2008',
        )

    def setUp(self):
        self.car = Car.objects.get(id=1)
        User = get_user_model()
        self.user = User.objects.create_user(
            username='Maxim',
            email='max@email.com',
            user_lang='en',
            password='testpass123'
        )

    def test_car_name_label(self):
        field_label = self.car._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'Название')

    def test_year_label(self):
        field_label = self.car._meta.get_field('year').verbose_name
        self.assertEquals(field_label,'Год')

    def test_owner_label(self):
        field_label = self.car._meta.get_field('owner').verbose_name
        self.assertEquals(field_label,'Владелец')

    def test_add_date_label(self):
        field_label = self.car._meta.get_field('add_date').verbose_name
        self.assertEquals(field_label,'Дата добавления')

    def test_car_name_max_length(self):
        max_length = self.car._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_car_name(self):
        expected_object_name = self.car.name
        self.assertEquals(expected_object_name, str(self.car))

    def test_object_name_car_names_on_diff_languages(self):
        name_en = self.car.name_en
        name_ru = self.car.name_ru
        self.assertEquals(name_en, 'Toyota')
        self.assertEquals(name_ru, self.car.name)

    def test_car_listing(self):
        self.assertEqual(f'{self.car.name}', 'Тойота')
        self.assertEqual(f'{self.car.year}', '2000')
        self.assertEqual(f'{self.car.owner}', 'None')

    def test_add_car_user(self):
        self.car.owner = self.user
        self.car.save()
        self.assertEqual(f'{self.car.owner}', 'Maxim')

    def test_custom_model_manager(self):
        self.car.owner = self.user
        self.car.save()
        car_2 = Car.objects.get(id=2)
        free_car = Car.free_cars.all()
        query = Car.objects.filter(owner=None)
        self.assertEqual(car_2, *free_car)
        self.assertQuerysetEqual(free_car, map(repr, query))

    def test_car_meta_names(self):
        name = Car._meta.verbose_name
        name_plural = Car._meta.verbose_name_plural
        self.assertEqual(name, 'Автомобиль')
        self.assertEqual(name_plural, 'Автомобили')

    def test_car_related_name(self):
        self.car.owner = self.user
        self.car.save()
        users_car = self.user.cars.all()[0]
        self.assertEqual(users_car, self.car)

    def test_database_queries_are_executed(self):
        with self.assertNumQueries(2):
            Car.objects.create(name="Lada", year="2018")
            Car.objects.create(name="BMW", year="2015", owner=self.user)
