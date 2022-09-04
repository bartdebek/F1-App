from django.test import TestCase
from django.urls import reverse, resolve
from .views import (DriversListView, 
                    DriversListCurrentView, 
                    DriversListPastView,)


class DriversListTests(TestCase):
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'drivers/driver_list.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self): 
        view = resolve("/")
        self.assertEqual(view.func.__name__, DriversListView.as_view().__name__)

    
class DriversListCurrentTests(TestCase):
    def setUp(self):
        url = reverse('driver_current')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'drivers/driver_current.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self): 
        view = resolve("/")
        self.assertEqual(view.func.__name__, DriversListCurrentView.as_view().__name__)

    
class DriversListPastTests(TestCase):
    def setUp(self):
        url = reverse('driver_past')
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'drivers/driver_past.html')

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_homepage_url_resolves_homepageview(self): 
        view = resolve("/")
        self.assertEqual(view.func.__name__, DriversListPastView.as_view().__name__)