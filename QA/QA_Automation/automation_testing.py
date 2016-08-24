from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

from unittest_data_provider import data_provider

import unittest
import random
import time
import csv


def csvParser():
	super_tuple = ()

	with open('data.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile)

		for row in reader:
			data_tuple = ()

			for data in row:
				data_tuple = data_tuple + (data.strip(),)

			super_tuple = super_tuple + (data_tuple,)

	#return super_tuple

	return (('25/8/2016', '26/8/2016', '1'),)


class AutomationTesting(unittest.TestCase):

	data_under_test = lambda : csvParser()


	def setUp(self):
		pass


	@data_provider(data_under_test)
	def test_automation(self, checkin_date, checkout_date, number_of_travellers):

		print checkin_date
		print checkout_date
		print number_of_travellers
		
		self.driver = webdriver.Firefox()		
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

		checkin = self.driver.find_element_by_id('metaCheckInSpan')
		checkin.click()

		calendar = self.driver.find_element_by_class_name('calendar')

		nav_prev_handler = calendar.find_element_by_xpath(".//span[@class = 'prev']/a")
		nav_next_handler = calendar.find_element_by_xpath(".//span[@class = 'next']/a")


		checkin_date = datetime.strptime(checkin_date, '%d/%m/%Y').date()
		print checkin_date

		current_checkin_date = checkin.find_element_by_id('checkIn').get_attribute('value')
		#current_checkin_date = datetime.strptime("28/2/2017", '%d/%m/%Y').date()
		current_checkin_date = datetime.strptime(current_checkin_date, '%d/%m/%Y').date()
		print current_checkin_date

		print current_checkin_date.month - checkin_date.month

		if checkin_date > current_checkin_date:
			month_diff = (checkin_date.year - current_checkin_date.year)*12 + (checkin_date.month - checkin_date.month)

			for x in range(month_diff):
				nav_next_handler.click()

		else:
			month_diff = (current_checkin_date.year - checkin_date.year)*12 + (current_checkin_date.month - checkin_date.month)

			for x in range(month_diff):
				nav_prev_handler.click()

	
		'''
		#checkout = self.driver.find_element_by_id('metaCheckOutSpan')
		#checkout.click()

		#calendar = self.driver.find_element_by_class_name('calendar')

		#nav_prev_handler = calendar.find_element_by_xpath(".//span[@class = 'prev']/a")
		#nav_next_handler = calendar.find_element_by_xpath(".//span[@class = 'next']/a")

	
		travellers = self.driver.find_element_by_id('fadults')
		travellers.click()

		options = travellers.find_elements_by_tag_name('option')

		for option in options:
			if option.get_attribute('value') == str(number_of_travellers): #user_value
				option.click()'''

		'''
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
				lambda : len(self.driver.window_handles) > 1
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

		flights = WebDriverWait(self.driver, 20).until(
			EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'taplc_flight_list_0']//div[@class = 'flightList']/div[@class = 'entry show']"))#//div[.//*[contains(text(), 'Musafir.com')]]//div[@class='mainButton']"))
		)


		flights = self.driver.find_elements_by_xpath("//div[@id = 'taplc_flight_list_0']//div[@class = 'flightList']/div[@class = 'entry show']")
		random_flight = random.choice(flights)

		self.driver.execute_script("return arguments[0].scrollIntoView();", random_flight)
		self.driver.execute_script("window.scrollBy(0, -150);")

		flight_booking_button = random_flight.find_element_by_xpath(".//div[@class = 'purchaseLinkColumn']//div[@class = 'mainButton']")
		
		amount_of_booking = random_flight.find_element_by_xpath(".//div[@class = 'purchaseLinkColumn']//span[@class = 'price']").text
		airline_name = random_flight.find_element_by_xpath(".//div[@class = 'flightInfoColumn']//div[@class = 'airlineName']").text

		flight_booking_button.click()
		self.driver.switch_to_window(self.driver.window_handles[0])

		print "Flight Details  ======================== "
		print "Airline Name :", airline_name
		print "Flight : ", amount_of_booking
		print "=========================================== "'''
		
		#self.driver.close()


	def tearDown(self):
		pass



if __name__ == "__main__":
	#AutomationTesting.number_of_travellers = 4
	unittest.main()