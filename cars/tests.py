from django.test import TestCase,SimpleTestCase
from django.urls import reverse, resolve
from django.utils.translation import activate

from .views import HomePageView
# Create your tests here.

class HomepageTests(SimpleTestCase):

    def test_homepage_redirect_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
    
    def test_homepage_en_status_code(self):
        activate('en')
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_homepage_template(self):
        activate('ru')
        response = self.client.get('/ru/')
        self.assertTemplateUsed(response, 'home.html')

    def test_uses_base_template(self):
        activate('en')
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "_base.html")
    
    def test_homepage_contains_correct_html(self):
        activate('en')
        response = self.client.get('/en/')
        self.assertContains(response, 'Homepage')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
    
    def test_homepage_does_not_contain_incorrect_html(self):
        activate('ru')
        response = self.client.get('/ru/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

        def test_homepage_url_resolves_homepageview(self):
            view = resolve('/ru/')
            self.assertEqual(
                view.func.__name__,
                HomePageView.as_view().__name__
            )
