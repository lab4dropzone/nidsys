from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3
class PageTest(LiveServerTestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()
   # def tearDown(self):
   #    self.browser.quit()

   def check_rows_in_listtable(self, row_text):
      start_time = time.time()
      while time.time()-start_time<cWait:
         # time.sleep(0.5)
         try:
            table = self.browser.find_element_by_id('registryTable')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])
            return
         except (AssertionError, WebDriverException) as e:
            if time.time()-start_time>cWait:
               raise e

   def test_another_entry_different_url(self):
      self.browser.get(self.live_server_url)
      self.assertIn('National ID System', self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('National Identification Registration System', headerText)
      inpSurname = self.browser.find_element_by_id('surname')
      inpFirstname = self.browser.find_element_by_id('firstname')
      inpMiddlename = self.browser.find_element_by_id('middlename')
      inpBdate = self.browser.find_element_by_id('bdate')
      inpAddress = self.browser.find_element_by_id('address')
      inpContactNo = self.browser.find_element_by_id('contactno')
      btnConfirm = self.browser.find_element_by_id('btnConfirm')
      self.assertEqual(inpSurname.get_attribute('placeholder'),'Enter surname here')
      time.sleep(0.5)
      inpSurname.click()
      time.sleep(0.1)
      inpSurname.send_keys('Mabanag')
      inpFirstname.click()
      time.sleep(0.1)
      inpFirstname.send_keys('Polo Jasty')
      inpMiddlename.click()
      time.sleep(0.1)
      inpMiddlename.send_keys('De Guzman')
      inpBdate.click()
      time.sleep(0.1)
      inpBdate.send_keys('03/01/2020')
      inpAddress.click()
      time.sleep(0.1)
      inpAddress.send_keys('Area 12 Silang Cavite')
      inpContactNo.click()
      time.sleep(0.1)
      inpContactNo.send_keys('0912-8761432')
      time.sleep(0.1) 
      btnConfirm.click()
      self.check_rows_in_listtable('1: Polo Jasty De Guzman Mabanag Status - pending')
      viewlist_url = self.browser.current_url
      self.assertRegex(viewlist_url, '/nidsys/.+')

      # self.browser.quit()
      # self.browser = webdriver.Firefox()
      # self.browser.get(self.live_server_url)
      # inpSurname = self.browser.find_element_by_id('surname')
      # inpFirstname = self.browser.find_element_by_id('firstname')
      # inpMiddlename = self.browser.find_element_by_id('middlename')
      # inpBdate = self.browser.find_element_by_id('bdate')
      # inpAddress = self.browser.find_element_by_id('address')
      # inpContactNo = self.browser.find_element_by_id('contactno')
      # btnConfirm = self.browser.find_element_by_id('btnConfirm')
      # self.assertEqual(inpSurname.get_attribute('placeholder'),'Enter surname here')
      # time.sleep(2)
      # inpSurname.click()
      # time.sleep(0.1)
      # inpSurname.send_keys('De Belen')
      # inpFirstname.click()
      # time.sleep(0.1)
      # inpFirstname.send_keys('Cyren Kate')
      # inpMiddlename.click()
      # time.sleep(0.1)
      # inpMiddlename.send_keys('Vee')
      # inpBdate.click()
      # time.sleep(0.1)
      # inpBdate.send_keys('01/21/2020')
      # inpAddress.click()
      # time.sleep(0.1)
      # inpAddress.send_keys('Area 33 Alfonso Cavite')
      # inpContactNo.click()
      # time.sleep(0.1)
      # inpContactNo.send_keys('0911-8723432')
      # time.sleep(0.1) 
      # btnConfirm.click()
      # self.check_rows_in_listtable('2: Cyren Kate Vee De Belen Status - pending')
      # viewlist_url2 = self.browser.current_url
      # self.assertRegex(viewlist_url2, '/nidsys/.+')
      # self.assertNotEqual(viewlist_url, viewlist_url2)
      # pageBody = self.browser.find_element_by_tag_name('body').text
      # self.assertIn('Polo Jasty De Guzman Mabanag', pageBody)
      # self.assertIn('Cyren Kate Vee De Belen', pageBody)
