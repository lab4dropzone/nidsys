from django.test import TestCase
'''
from nidsys.views import MainPage
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string'''

class HomePageTest(TestCase):
   def test_mainpage_template_ba_gamit(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response,'mainpage.html')
   """
   def test_root_url_resolves_to_mainpage_view(self):
      found = resolve('/')
      self.assertEqual(found.func, MainPage)
      
   def test_mainpage_responding_view(self):
      '''(second)
      request = HttpRequest()
      response = MainPage(request)
      '''
      response = self.client.get('/')
      html = response.content.decode('utf8')
      ''' (first)
      self.assertTrue(html.startswith('<!DOCTYPE html>'))
      self.assertIn('<title>National ID System</title>', html)
      self.assertTrue(html.endswith(''))
      '''
      string_html = render_to_string('mainpage.html')
      self.assertEqual(html, string_html)
      self.assertTemplateUsed(response,'mainpage.html')
      """
   

