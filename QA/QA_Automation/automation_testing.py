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
		element.clear()
		element.send_keys("Pune")


		element = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//ul[@class = 'autocompleter-choices flights'][1]"))
			)

		option = element.find_element_by_class_name('autocompleter-selected')
		option.click()

		

		element = self.driver.find_element_by_id('metaFlightTo')
		element.clear()
		element.send_keys("Delhi")

		element = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//ul[@class = 'autocompleter-choices flights'][2]"))
			)

		option = element.find_element_by_class_name('autocompleter-selected')
		option.click()

		#element = self.driver.find_element_by_id('checkIn')
		#element.click()


		#element = self.driver.find_element_by_id('checkOut')
		#element.click()

		element = self.driver.find_element_by_id('fadults')
		element.click()

		options = element.find_elements_by_tag_name('option')

		for option in options:
			if option.get_attribute('value') == "2": #user_value
				option.click()

		
		element = self.driver.find_element_by_id('SUBMIT_FLIGHTS')
		element.click()

		try:
			element = WebDriverWait(self.driver, 10).until(
					EC.visibility_of_element_located((By.CLASS_NAME, "ui_modal"))
				)

			close = element.find_element_by_xpath("//div[@class = 'ui_close_x']")
			close.click()

		except :

			print "No pop up !"


		print self.driver.window_handles

		if len(self.driver.window_handles) > 1:
			for x in range(1, len(self.driver.window_handles)):
				self.driver.switch_to_window(self.driver.window_handles[x])
				self.driver.close()

		self.driver.switch_to_window(self.driver.window_handles[0])

		element = WebDriverWait(self.driver, 20).until(
				EC.visibility_of_element_located((By.XPATH, "//div[@id = 'taplc_flight_results_sorts_0']/descendant::span[@class = 'sort_item sort_item_more']/label"))
			)

		element.click()


		#filters = self.driver.find_elements_by_xpath("//div[@id = 'sort_sub_items']/div[@class = 'sub_sort_item']")

		#filters.find_element_by_tag_name('label').click()

		filters = self.driver.find_element_by_xpath("//div[@id = 'sort_sub_items']/div[@class = 'sub_sort_item']/label")
		filters.click()









	#def tearDown(self):
	#	self.driver.close()


if __name__ == "__main__":
	unittest.main()