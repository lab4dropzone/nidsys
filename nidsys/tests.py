from django.urls import resolve
from django.test import TestCase
from nidsys.views import MainPage

from django.http import HttpRequest

class HomePageTest(TestCase):
   def test_root_url_resolves_to_mainpage_view(self):
      found = resolve('/')
      self.assertEqual(found.func, MainPage)
      
   def test_mainpage_if_responding_view(self):
      request = HttpRequest()
      response = MainPage(request)
      html = response.content.decode('utf8')
      self.assertTrue(html.startswith('<html>'))
      self.assertIn('<title>National ID System</title>', html)
      self.assertTrue(html.endswith('</html>'))
