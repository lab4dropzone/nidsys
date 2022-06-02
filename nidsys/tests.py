'''
from nidsys.views import MainPage
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string'''
from django.test import TestCase
from nidsys.models import Registration

class HomePageTest(TestCase):
   def test_mainpage_template_ba_gamit(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response,'mainpage.html')
   
   # def test_only_saves_items_if_necessary(self):
   #    self.client.get('/')
   #    self.assertEqual(Registration.objects.count(), 0)

class CreateListTest(TestCase):
   def test_save_POST_request(self):
      response = self.client.post('/nidsys/newlist_url', data={'surname': 'newSurname',
         'firstname': 'newFirstname','middlename': 'newMiddlename','bdate':'newBdate',
         'address': 'newAddress','contactno': 'newContactNo'})
      self.assertEqual(Registration.objects.count(), 1)
      newEntry = Registration.objects.first()
      self.assertEqual(newEntry.sname, 'newSurname')
      
   def test_POST_redirect(self):
      response = self.client.post('/nidsys/newlist_url', data={'surname': 'newSurname',
         'firstname': 'newFirstname','middlename': 'newMiddlename','bdate':'newBdate',
         'address': 'newAddress','contactno': 'newContactNo'})
      self.assertRedirects(response, '/nidsys/viewlist_url/')
      # self.assertEqual(response.status_code, 302)
      # self.assertEqual(response['location'], '/nidsys/viewlist_url/')
      # self.assertEqual(response['location'], '/')


   # def test_template_displays_list(self):
   #    Registration.objects.create(sname='Maliksi')
   #    Registration.objects.create(sname='Balota')
   #    response = self.client.get('/')
   #    self.assertIn('Maliksi', response.content.decode())
   #    self.assertIn('Balota', response.content.decode())

class ViewTest(TestCase):
   def test_displays_all(self):
      Registration.objects.create(fname='Cyren Kate De Belen')
      Registration.objects.create(fname='Acey Aljorie Ponilas')
      response = self.client.get('/nidsys/viewlist_url/')
      self.assertContains(response, 'Cyren Kate De Belen')
      self.assertContains(response, 'Acey Aljorie Ponilas')

   def test_listview_uses_listpage(self):
      response = self.client.get('/nidsys/viewlist_url/')
      self.assertTemplateUsed(response, 'listpage.html')

class ORMTest(TestCase):
   def test_saving_retrieving_list(self):
      entry1 = Registration()
      entry1.idno = '202004210001002345'
      entry1.fname = 'Cyren Kate'
      entry1.mname = 'Vie'
      entry1.sname = 'De Belen'
      entry1.bdate = '03/05/2020'
      entry1.address = 'Area 12 Dasmarinas Cavite '
      entry1.contactno = '0987-1234567'
      entry1.save()
      entry2 = Registration()
      entry2.idno = '202105250001002346'
      entry2.fname = 'Acey Aljorie'
      entry2.mname = 'Veral'
      entry2.sname = 'Ponilas'
      entry1.bdate = '06/15/2021'
      entry2.address = 'Area 35 Tagaytay Cavite '
      entry2.contactno = '0912-4324567'
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
   

