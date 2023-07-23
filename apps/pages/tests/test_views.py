from django.test import TestCase
from django.urls import reverse

class HomePageViewTest(TestCase):
    def test_home_page_view_should_return_200(self):
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')

class AboutPageViewTest(TestCase):
    def test_about_page_view_should_return_200(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/about.html')
