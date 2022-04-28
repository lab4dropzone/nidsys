from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time
from django.test import LiveServerTestCase

cWait = 3
class PageTest(LiveServerTestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()
   # def tearDown(self):
   #    self.browser.quit()

   def check_rows_in_listtable(self, row_text):
      start_time = time.time()
      while time.time()-start_time<cWait:
         # time.sleep(0.1)
         try:
            table = self.browser.find_element_by_id('registryTable')
            rows = table.find_elements_by_tag_name('tr')
            self.assertIn(row_text, [row.text for row in rows])
            return
         except (AssertionError, WebDriverException) as e:
            if time.time()-start_time>cWait:
               raise e

      # table = self.browser.find_element_by_id('registryTable')
      # rows = table.find_elements_by_tag_name('tr')
      # self.assertIn(row_text, [row.text for row in rows])

   def test_application_and_review(self):
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
      inpSurname.click()
      time.sleep(0.5)
      inpSurname.send_keys('Delos Santos')
      inpFirstname.click()
      time.sleep(0.5)
      inpFirstname.send_keys('Ralph')
      inpMiddlename.click()
      time.sleep(0.5)
      inpMiddlename.send_keys('Dee')
      inpBdate.click()
      time.sleep(0.5)
      inpBdate.send_keys('02/03/2020')
      inpAddress.click()
      time.sleep(0.5)
      inpAddress.send_keys('B1 L11 Area 51 Dasmarinas Cavite')
      inpContactNo.click()
      time.sleep(0.5)
      inpContactNo.send_keys('0987-6543210')
      time.sleep(0.5) 
      btnConfirm.click()

      # self.check_rows_in_listtable('1: Polo Jasty De Guzman Mabanag Status - pending')
      self.check_rows_in_listtable('1: Ralph Dee Delos Santos Status - pending')
      
      # table = self.browser.find_element_by_id('registryTable')
      # rows = table.find_elements_by_tag_name('tr')
      # self.assertIn('1: Ralph Dee Delos Santos', [row.text for row in rows])
      #self.fail('Finish the test!')

   def test_another_entry(self):
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
      time.sleep(2)
      inpSurname.click()
      time.sleep(0.5)
      inpSurname.send_keys('Mabanag')
      inpFirstname.click()
      time.sleep(0.5)
      inpFirstname.send_keys('Polo Jasty')
      inpMiddlename.click()
      time.sleep(0.5)
      inpMiddlename.send_keys('De Guzman')
      inpBdate.click()
      time.sleep(0.5)
      inpBdate.send_keys('03/05/2020')
      inpAddress.click()
      time.sleep(0.5)
      inpAddress.send_keys('Area 52 Silang Cavite')
      inpContactNo.click()
      time.sleep(0.5)
      inpContactNo.send_keys('0912-8765432')
      time.sleep(0.5) 
      btnConfirm.click()
      
      self.check_rows_in_listtable('1: Polo Jasty De Guzman Mabanag Status - pending')
      
   #    table = self.browser.find_element_by_id('registryTable')
   #    rows = table.find_elements_by_tag_name('tr')
   #    self.assertIn('1: Ralph Dee Delos Santos', [row.text for row in rows])
      #self.fail('Finish the test!')
      
# if __name__ == '__main__':
#       unittest.main(warnings='ignore')
      
