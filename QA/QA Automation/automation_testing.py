from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import unittest

class AutomationTesting(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_automation(self):
		self.driver.get("https://www.tripadvisor.in")
		element = self.driver.find_element_by_id('rdoFlights')
		element.click()

		element = self.driver.find_element_by_id('metaFlightFrom')
		element.send_keys("Pune")

		
		#element = WebDriverWait(self.driver, 10).until(
		#		EC.presence_of_element_located((By.))
		#	)

		element = self.driver.find_element_by_id('metaFlightTo')
		element.send_keys("Delhi")

		element = self.driver.find_element_by_id('SUBMIT_FLIGHTS')
		element.click()


	def tearDown(self):
		self.driver.close()


if __name__ == "__main__":
	unittest.main()