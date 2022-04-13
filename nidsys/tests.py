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


   def test_save_POST_request(self):
      response = self.client.post('/', data={'surname': 'newSurname',
         'firstname': 'newFirstname','middlename': 'newMiddlename',
         'address': 'newAddress','contactno': 'newContactNo'})
      self.assertIn('newSurname', response.content.decode())
      self.assertTemplateUsed(response,'mainpage.html')
      
from nidsys.models import Registration
class ORMTest(TestCase):
   def test_saving_retrieving_list(self):
      entry1 = Registration()
      entry1.idno = '000001002345'
      entry1.fname = 'Cyren Kate'
      entry1.mname = 'Vie'
      entry1.sname = 'De Belen'
      entry1.address = 'Area 12 Dasmarinas Cavite '
      entry1.contactno = '0987-1234567'
      entry1.status = 'pending'
      entry1.save()
      entry2 = Registration()
      entry2.idno = '000001002346'
      entry2.fname = 'Acey Aljorie'
      entry2.mname = 'Veral'
      entry2.sname = 'Ponilas'
      entry2.address = 'Area 35 Tagaytay Cavite '
      entry2.contactno = '0912-4324567'
      entry2.status = 'pending'
      entry2.save()
      items = Registration.objects.all()
      self.assertEqual(items.count(), 2)
      items1 = items[0]
      items2 = items[1]
      self.assertEqual(items1.fname, 'Cyren Kate')
      self.assertEqual(items2.fname, 'Acey Aljorie')  

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
   

