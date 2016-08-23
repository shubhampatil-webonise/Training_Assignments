from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import unittest
import random
import time

class AutomationTesting(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()

	def test_automation(self):
		
		self.driver.get("https://www.tripadvisor.in")

		flights_tab_button = self.driver.find_element_by_id('rdoFlights')
		flights_tab_button.click()

		flight_source_input = self.driver.find_element_by_id('metaFlightFrom')
		flight_source_input.clear()
		flight_source_input.send_keys("Pune")

		source_choices_dropdown = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//ul[@class = 'autocompleter-choices flights'][1]"))
			)

		source_choice_selected = source_choices_dropdown.find_element_by_class_name('autocompleter-selected')
		source_choice_selected.click()

		flight_destination_input = self.driver.find_element_by_id('metaFlightTo')
		flight_destination_input.clear()
		flight_destination_input.send_keys("Delhi")

		destination_choice_dropdown = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//ul[@class = 'autocompleter-choices flights'][2]"))
			)

		destination_choice_selected = destination_choice_dropdown.find_element_by_class_name('autocompleter-selected')
		destination_choice_selected.click()

		#element = self.driver.find_element_by_id('checkIn')
		#element.click()


		#element = self.driver.find_element_by_id('checkOut')
		#element.click()

		number_of_travellers = self.driver.find_element_by_id('fadults')
		number_of_travellers.click()

		options = number_of_travellers.find_elements_by_tag_name('option')

		for option in options:
			if option.get_attribute('value') == "2": #user_value
				option.click()

		self.driver.execute_script("window.scrollTo(0,0)")

		search_button = self.driver.find_element_by_id('SUBMIT_FLIGHTS')
		search_button.click()

		try:
			popup_modal = WebDriverWait(self.driver, 10).until(
					EC.visibility_of_element_located((By.CLASS_NAME, "ui_modal"))
				)

			close_button = popup_modal.find_element_by_xpath(".//div[@class = 'ui_close_x']")
			close_button.click()

		except :

			print "No pop up !"


		WebDriverWait(self.driver, 10).until(
				lambda driver: len(self.driver.window_handles) > 1
			)


		for x in range(1, len(self.driver.window_handles)):
			self.driver.switch_to_window(self.driver.window_handles[x])
			self.driver.close()

		self.driver.switch_to_window(self.driver.window_handles[0])

		more_sort_filter = WebDriverWait(self.driver, 60).until(
				EC.visibility_of_element_located((By.XPATH, "//div[@id = 'taplc_flight_results_sorts_0']/descendant::span[@class = 'sort_item sort_item_more']/label"))
			)

		more_sort_filter.click()

		sort_filters =  WebDriverWait(self.driver, 10).until(
				EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'sort_sub_items']/div[@class = 'sub_sort_item']"))
			)

		selected_filter = random.choice(sort_filters)
		selected_filter.find_element_by_tag_name('label').click()

		WebDriverWait(self.driver, 10).until(
			EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'loadingOverlay']"))
		)

		elements = WebDriverWait(self.driver, 10).until(
			EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'taplc_flight_list_0']/descendant::div[@class = 'flightList']/div[@class = 'entry show']//div[@class='mainButton']"))
		)

		print len(elements)

		''' 

		flight_booking_buttons = self.driver.find_elements_by_xpath("//div[@id = 'taplc_flight_list_0']/descendant::div[@class = 'flightList']/div[@class = 'entry show']//div[@class='mainButton']")


		#random_flight_button = random.choice(flight_booking_buttons)
		
		
		button = WebDriverWait(self.driver, 10).until(
				EC.element_to_be_clickable((By.XPATH, "//div[@id = 'taplc_flight_list_0']/descendant::div[@class = 'flightList']/div[@class = 'entry show']//div[@class='mainButton']"))
			)



		button.click()'''

		'''flight_list = WebDriverWait(self.driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//div[@id = 'taplc_flight_list_0']/descendant::div[@class = 'flightList']"))
			)

		print flight_list.text'''


		'''flight_list = WebDriverWait(self.driver, 10).until(
				##EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'taplc_flight_list_0']/descendant::div[@class = 'flightList']/div[@class = 'entry show']"))

			)'''

		#print "total flights ==================" , len(flight_list)

		'''random_flight = random.choice(flight_list)

		print "Flight ===================", random_flight.text

		flight_booking_button = random_flight.find_element_by_xpath(".//descendant::div[@class = 'purchaseLinkColumn']/a[1]")#/div[@class = 'mainButton']")

		print "==========================", flight_booking_button.text
		flight_booking_button.click()'''

		#flight_booking_button = WebDriverWait(self.driver, 10).until(
		#		EC.element_to_be_clickable((By.XPATH, "//div[@class = 'purchaseLinkColumn']/a/div[@class = 'mainButton']"))
		#	)		

		#flight_booking_button.click()

		#flight_booking_button = random_flight.find_element_by_xpath("//div[@class = 'purchaseLinkColumn']/a/div[@class = 'mainButton']")
		#flight_booking_button.click()


		'''flight_list = self.driver.find_elements_by_xpath("//div[@id = 'taplc_flight_list_0']/descendant::div[@class = 'flightList']/div[@class = 'entry show']")
		random_flight = random.choice(flight_list)

		flight_booking_button = random_flight.find_element_by_xpath("//div[@class = 'purchaseLinkColumn']/a/div[@class = 'mainButton']")
		print flight_booking_button.get_attribute('class')
		#flight_booking_button.click()'''




	#def tearDown(self):
	#	self.driver.close()


if __name__ == "__main__":
	unittest.main()