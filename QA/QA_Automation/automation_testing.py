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

	return super_tuple


def select_flight_tab(driver):
	
	flights_tab_button = driver.find_element_by_id('rdoFlights')
	flights_tab_button.click()


def set_source_and_destination(driver):

	flight_source_input = driver.find_element_by_id('metaFlightFrom')
	flight_source_input.clear()
	flight_source_input.send_keys("Pune")

	try:
		source_choices_dropdown = WebDriverWait(driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//ul[@class = 'autocompleter-choices flights'][1]"))
			)

	except:
		flight_source_input.send_keys(Keys.TAB)


	source_choice_selected = source_choices_dropdown.find_element_by_class_name('autocompleter-selected')
	source_choice_selected.click()

	flight_destination_input = driver.find_element_by_id('metaFlightTo')
	flight_destination_input.clear()
	flight_destination_input.send_keys("Delhi")

	try:
		destination_choice_dropdown = WebDriverWait(driver, 10).until(
				EC.visibility_of_element_located((By.XPATH, "//ul[@class = 'autocompleter-choices flights'][2]"))
			)

	except:
		flight_destination_input.send_keys(Keys.TAB)


	destination_choice_selected = destination_choice_dropdown.find_element_by_class_name('autocompleter-selected')
	destination_choice_selected.click()



def set_flight_dates(driver, id, check_date):

	date_input = driver.find_element_by_id(id)
	date_input.click()

	calendar = driver.find_element_by_class_name('calendar')

	check_date = datetime.strptime(check_date, '%d/%m/%Y').date()

	if id == 'metaCheckInSpan':
		current_check_date = date_input.find_element_by_id('checkIn').get_attribute('value')
	else:
		current_check_date = date_input.find_element_by_id('checkOut').get_attribute('value')


	current_check_date = datetime.strptime(current_check_date, '%d/%m/%Y').date()

	month_and_year = check_date.strftime('%B') + " " + check_date.strftime('%Y')
	date = check_date.strftime('%d')

	if check_date > current_check_date:

		while( month_and_year not in calendar.text):

			nav_next_handler = WebDriverWait(driver, 5).until(
					EC.element_to_be_clickable((By.XPATH, ".//span[@class = 'next']/a"))
				)

			nav_next_handler.click()
			time.sleep(2)

		calendar_date = WebDriverWait(driver, 5).until(
				EC.element_to_be_clickable((By.XPATH, ".//div[@class = 'calendar']//div[.//*[contains(text(), '"+ month_and_year +"')]]//*[contains(text(), '"+ date +"')]"))
			)

		calendar_date.click()


	else:

		while( month_and_year not in calendar.text):
			
			nav_prev_handler = WebDriverWait(driver, 5).until(
					EC.element_to_be_clickable((By.XPATH, ".//span[@class = 'prev']/a"))
				)

			nav_prev_handler.click()
			time.sleep(2)


		calendar_date = WebDriverWait(driver, 5).until(
				EC.element_to_be_clickable((By.XPATH, ".//div[@class = 'calendar']//div[.//*[contains(text(), '"+ month_and_year +"')]]//*[contains(text(), '"+ date +"')]"))
			)

		calendar_date.click()



def set_number_of_travellers(driver, number_of_travellers):
	travellers = driver.find_element_by_id('fadults')
	travellers.click()

	options = travellers.find_elements_by_tag_name('option')

	for option in options:
		if option.get_attribute('value') == str(number_of_travellers): #user_value
			option.click()

	driver.execute_script("window.scrollTo(0,0)")



def handle_popups(driver):
	print "waiting for popup"

	try:
		popup_modal = WebDriverWait(driver, 30).until(
				EC.visibility_of_element_located((By.XPATH, ".//*[@class = 'ui_overlay ui_modal no_padding']"))
			)

		close_button = popup_modal.find_element_by_xpath(".//div[@class = 'ui_close_x']")
		close_button.click()

	except :

		print "No pop up !"

	driver = driver
	
	WebDriverWait(driver, 10).until(
			lambda driver : len(driver.window_handles) > 1
		)


	for x in range(1, len(driver.window_handles)):
		driver.switch_to_window(driver.window_handles[x])
		driver.close()

	driver.switch_to_window(driver.window_handles[0])



def select_random_filter(driver):

	more_sort_filter = WebDriverWait(driver, 60).until(
			EC.visibility_of_element_located((By.XPATH, "//div[@id = 'taplc_flight_results_sorts_0']/descendant::span[@class = 'sort_item sort_item_more']/label"))
		)

	more_sort_filter.click()

	sort_filters =  WebDriverWait(driver, 10).until(
			EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'sort_sub_items']/div[@class = 'sub_sort_item']"))
		)

	selected_filter = random.choice(sort_filters)
	selected_filter.find_element_by_tag_name('label').click()

	WebDriverWait(driver, 10).until(
		EC.invisibility_of_element_located((By.XPATH, "//div[@id = 'loadingOverlay']"))
	)


def select_random_flight(driver):

	flights = WebDriverWait(driver, 20).until(
		EC.presence_of_all_elements_located((By.XPATH, "//div[@id = 'taplc_flight_list_0']//div[@class = 'flightList']/div[@class = 'entry show']"))#//div[.//*[contains(text(), 'Musafir.com')]]//div[@class='mainButton']"))
	)


	flights = driver.find_elements_by_xpath("//div[@id = 'taplc_flight_list_0']//div[@class = 'flightList']/div[@class = 'entry show']")
	random_flight = random.choice(flights)

	driver.execute_script("return arguments[0].scrollIntoView();", random_flight)
	driver.execute_script("window.scrollBy(0, -150);")

	flight_booking_button = random_flight.find_element_by_xpath(".//div[@class = 'purchaseLinkColumn']//div[@class = 'mainButton']")
	
	amount_of_booking = random_flight.find_element_by_xpath(".//div[@class = 'purchaseLinkColumn']//span[@class = 'price']").text
	airline_name = random_flight.find_element_by_xpath(".//div[@class = 'flightInfoColumn']//div[@class = 'airlineName']").text

	flight_booking_button.click()
	driver.switch_to_window(driver.window_handles[0])

	print "\n\nFlight Details  ======================== "
	print "Airline Name :", airline_name
	print "Flight : ", amount_of_booking
	print "=========================================== "




class AutomationTesting(unittest.TestCase):

	data_under_test = lambda : csvParser()


	def setUp(self):
		pass


	@data_provider(data_under_test)
	def test_flow_of_tripadvisor_dot_in(self, checkin_date, checkout_date, number_of_travellers):

		
		self.driver = webdriver.Firefox()		
		self.driver.get("https://www.tripadvisor.in")

		self.assertEqual( self.driver.title, "TripAdvisor: Read Reviews, Compare Prices & Book")
		self.assertTrue( "Find and book your ideal trip at the lowest prices" in self.driver.find_element_by_id('taplc_brand_homepage_header_box_0').text)
		self.assertTrue( "Millions of traveller reviews and photos to help you get it right." in self.driver.find_element_by_id('taplc_brand_homepage_header_box_0').text)

		select_flight_tab(self.driver)		
		set_source_and_destination(self.driver)

		set_flight_dates(self.driver, 'metaCheckInSpan', checkin_date)
		set_flight_dates(self.driver, 'metaCheckOutSpan', checkout_date)

		set_number_of_travellers(self.driver, number_of_travellers)

		search_button = self.driver.find_element_by_id('SUBMIT_FLIGHTS')
		search_button.click()


		self.assertEqual(self.driver.title, "Cheap flights to New Delhi (DEL) - TripAdvisor")
		self.assertTrue("Pune" in self.driver.find_element_by_class_name('topBar').text)
		self.assertTrue("New Delhi" in self.driver.find_element_by_class_name('topBar').text)
		self.assertTrue("Prices include taxes and fees, so you'll know the real cost up front." in self.driver.find_element_by_id('taplc_flight_search_price_disclaimer_0').text)


		handle_popups(self.driver)
		select_random_filter(self.driver)

		select_random_flight(self.driver)
		
		self.driver.close()


	def tearDown(self):
		pass



if __name__ == "__main__":
	unittest.main()