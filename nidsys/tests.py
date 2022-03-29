from django.urls import resolve
from django.test import TestCase
from nidsys.views import MainPage

class HomePageTest(TestCase):
   def test_root_url_resolves_to_mainpage_view(self):
      found = resolve('/')
      self.assertEqual(found.func, MainPage)
