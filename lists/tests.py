from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
# Create your tests here.

class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
