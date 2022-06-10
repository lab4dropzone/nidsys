from django.test import TestCase
from nidsys.models import Registration, PreviousAddr

class HomePageTest(TestCase):
   def test_mainpage_template_ba_gamit(self):
      response = self.client.get('/')
      self.assertTemplateUsed(response,'mainpage.html')

class CreateListTest(TestCase):
   def test_save_POST_request(self):
      response = self.client.post('/nidsys/newlist_url', data={'surname':'De Belen','firstname':'Cyren Kate',
         'middlename':'Vie','bdate':'May 5, 1999','address':'Bailen Cavite','contactno':'0912665312'})
      self.assertEqual(Registration.objects.count(), 1)
      newEntry = Registration.objects.first()
      self.assertEqual(newEntry.sname,'De Belen')
      
   def test_POST_redirect(self):
      response = self.client.post('/nidsys/newlist_url', data={'surname':'De Belen','firstname':'Cyren Kate',
         'middlename':'Vie','bdate':'May 5, 1999','address':'Bailen Cavite','contactno':'0912665312'})
      self.assertEqual(Registration.objects.count(), 1)
      newReg = Registration.objects.first()
      self.assertRedirects(response,f'/nidsys/{newReg.id}/')

class ViewTest(TestCase):
   def test_displays_for_each_reg(self):
      mregid1 = Registration.objects.create(idno="2022058712",fname="Cyren Kate",sname="De Belen")
      PreviousAddr.objects.create(regid=mregid1,prevaddr="Bailen Cavite",fromdate="May 23,2020",todate="June 12, 1997")
      PreviousAddr.objects.create(regid=mregid1,prevaddr="Alfonso Cavite",fromdate="September 23,2020",todate="March 12, 1997")
      mregid2 = Registration.objects.create(idno="3122058712",fname="Acey Aljorie",sname="Ponilas")
      PreviousAddr.objects.create(regid=mregid2,prevaddr="Dasmarinas Cavite",fromdate="May 23,2020",todate="June 12, 1997")
      PreviousAddr.objects.create(regid=mregid2,prevaddr="Tagaytay Cavite",fromdate="September 23,2020",todate="March 12, 1997")
      response = self.client.get(f'/nidsys/{mregid1.id}/')
      self.assertContains(response,'Bailen Cavite')
      self.assertContains(response,'Alfonso Cavite')
      self.assertNotContains(response,'Dasmarinas Cavite')
      self.assertNotContains(response,'Tagaytay Cavite')
      response = self.client.get(f'/nidsys/{mregid2.id}/')
      self.assertNotContains(response,'Bailen Cavite')
      self.assertNotContains(response,'Alfonso Cavite')
      self.assertContains(response,'Dasmarinas Cavite')
      self.assertContains(response,'Tagaytay Cavite')

   def test_listview_uses_listpage(self):
      newReg = Registration.objects.create()
      response = self.client.get(f'/nidsys/{newReg.id}/')
      self.assertTemplateUsed(response, 'listpage.html')

   def test_pass_list_to_template(self):
      reg1 = Registration.objects.create()
      passList = Registration.objects.create()
      reg2 = Registration.objects.create()
      response = self.client.get(f'/nidsys/{passList.id}/')
      self.assertEqual(response.context['regId'],passList)

class AddPrevAddrTest(TestCase):
   def test_add_POST_request_to_existing_Registrant(self):
      Reg111= Registration.objects.create()
      exReg = Registration.objects.create()
      Reg222 = Registration.objects.create()
      self.client.post(f'/nidsys/{exReg.id}/addList',data={'prevaddr':'Salitran Dasmarinas Cavite',
         'fromdate': 'July 5, 1998','todate':'December 15, 2000'})
      self.assertEqual(PreviousAddr.objects.count(), 1)
      newList = PreviousAddr.objects.first()
      self.assertEqual(newList.prevaddr, 'Salitran Dasmarinas Cavite')
      self.assertEqual(newList.regid, exReg)

   def test_redirects_to_list_view(self):
      Reg111 = Registration.objects.create()
      exReg = Registration.objects.create()
      Reg222 = Registration.objects.create()
      Reg333 = Registration.objects.create()
      response = self.client.post(f'/nidsys/{exReg.id}/addList',data={'prevaddr':'GMA Cavite',
         'fromdate': 'April 15, 1998','todate':'October 9, 2000'})
      self.assertRedirects(response, f'/nidsys/{exReg.id}/')

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
