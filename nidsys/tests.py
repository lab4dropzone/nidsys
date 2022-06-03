from django.test import TestCase
from nidsys.models import Registration, PreviousAddr

class HomePageTest(TestCase):
   def test_mainpage_template_ba_gamit(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response,'mainpage.html')

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

class ViewTest(TestCase):
   # def test_displays_all(self):
   #    Registration.objects.create(fname='Cyren Kate De Belen')
   #    Registration.objects.create(fname='Acey Aljorie Ponilas')
   #    response = self.client.get('/nidsys/viewlist_url/')
   #    self.assertContains(response, 'Cyren Kate De Belen')
   #    self.assertContains(response, 'Acey Aljorie Ponilas')

   def test_listview_uses_listpage(self):
      response = self.client.get('/nidsys/viewlist_url/')
      self.assertTemplateUsed(response, 'listpage.html')

class ORMTest(TestCase):
   def test_saving_retrieving_list(self):  
      newReg = Registration()
      newReg.idno = '202004210001002345'
      newReg.fname = 'Cyren Kate'
      newReg.mname = 'Vie'
      newReg.sname = 'De Belen'
      newReg.bdate = '04/21/2020'
      newReg.address = 'Area 12 Dasmarinas Cavite '
      newReg.contactno = '0987-1234567'
      newReg.save()
      listItem1 = PreviousAddr()
      listItem1.regid = newReg #primkey-.id attrib
      listItem1.prevaddr = 'Area 33 Bailen Cavite'
      listItem1.fromdate = 'May 23, 2008'
      listItem1.todate = 'September 5, 2021' 
      listItem1.save()
      listItem2 = PreviousAddr()
      listItem2.regid = newReg
      listItem2.prevaddr = 'Salawag Dasmarinas Cavite'
      listItem2.fromdate = 'January 23, 2001'
      listItem2.todate = 'September 15, 2007' 
      listItem2.save()
      savedReg = Registration.objects.first()
      self.assertEqual(savedReg, newReg)
      savedPrevAddr = PreviousAddr.objects.all()
      self.assertEqual(savedPrevAddr.count(), 2)
      savedPrevAddr1 = savedPrevAddr[0]
      savedPrevAddr2 = savedPrevAddr[1]
      self.assertEqual(savedPrevAddr1.prevaddr, 'Area 33 Bailen Cavite')
      self.assertEqual(savedPrevAddr2.prevaddr, 'Salawag Dasmarinas Cavite')
      self.assertEqual(savedPrevAddr1.fromdate, 'May 23, 2008')
      self.assertEqual(savedPrevAddr2.fromdate, 'January 23, 2001')
      self.assertEqual(savedPrevAddr1.regid, newReg)
      self.assertEqual(savedPrevAddr2.regid, newReg)

   # def test_saving_retrieving_list(self):
   #    entry1 = Registration()
   #    entry1.idno = '202004210001002345'
   #    entry1.fname = 'Cyren Kate'
   #    entry1.mname = 'Vie'
   #    entry1.sname = 'De Belen'
   #    entry1.bdate = '03/05/2020'
   #    entry1.address = 'Area 12 Dasmarinas Cavite '
   #    entry1.contactno = '0987-1234567'
   #    entry1.save()
   #    entry2 = Registration()
   #    entry2.idno = '202105250001002346'
   #    entry2.fname = 'Acey Aljorie'
   #    entry2.mname = 'Veral'
   #    entry2.sname = 'Ponilas'
   #    entry1.bdate = '06/15/2021'
   #    entry2.address = 'Area 35 Tagaytay Cavite '
   #    entry2.contactno = '0912-4324567'
   #    entry2.save()
   #    items = Registration.objects.all()
   #    self.assertEqual(items.count(), 2)
   #    items1 = items[0]
   #    items2 = items[1]
   #    self.assertEqual(items1.fname, 'Cyren Kate')
   #    self.assertEqual(items2.fname, 'Acey Aljorie') 
