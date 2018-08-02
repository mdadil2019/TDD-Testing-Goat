from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
# Create your tests here.

class HomePageTest(TestCase):
    def test_use_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    # in order to add item to the list we have to post the request so here we are testing our future code
    def test_can_save_post_request(self):
        response = self.client.post('/',data = {"item_text" : "A new list item"})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response,'home.html')
