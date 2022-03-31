from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import unittest
import time

class PageTest(unittest.TestCase):
   def setUp(self):
      self.browser = webdriver.Firefox()
   # def tearDown(self):
   #    self.browser.quit()

   def test_application_and_review(self):
      self.browser.get('http://localhost:8000')
      self.assertIn('National ID System', self.browser.title)
      headerText = self.browser.find_element_by_tag_name('h1').text
      self.assertIn('National Identification Registration System', headerText)
      inpSurname = self.browser.find_element_by_id('surname')
      inpFirstname = self.browser.find_element_by_id('firstname')
      inpMiddlename = self.browser.find_element_by_id('middlename')
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
      inpAddress.click()
      time.sleep(0.5)
      inpAddress.send_keys('B1 L11 Area 51 Dasmarinas Cavite')
      inpContactNo.click()
      time.sleep(0.5)
      inpContactNo.send_keys('0987-6543210')
      time.sleep(0.5)
        
      btnConfirm.click()
      '''
      table = self.browser.find_element_by_id('idListTable')
      rows = table.find_elements_by_tag_name('tr')
      self.assertTrue(any(row.text == '1: Mickey Mouse'),"Wala ka pang table!")
      #self.fail('Finish the test!')
      '''
      
if __name__ == '__main__':
      unittest.main(warnings='ignore')
      
