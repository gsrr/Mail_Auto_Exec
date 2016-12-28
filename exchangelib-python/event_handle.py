# -*- coding: utf-8 -*-
import time
from selenium import webdriver

def browse_select_option(driver, elem_name):
	#element = driver.find_element_by_name("adultCount")
	element = driver.find_element_by_name(elem_name)
	all_options = element.find_elements_by_tag_name("option")
	for option in all_options:
		print("Value is: %s" % option.get_attribute("value"))
		option.click()

def click_submit_by_name(driver, elem_name):
	#search_box = driver.find_element_by_name('submitButtonName_intwws')
	search_box = driver.find_element_by_name(elem_name)
	search_box.click()
    
def click_submit_by_id(driver, elem_id):
	search_box = driver.find_element_by_id(elem_id)
	search_box.click()
    
def fill_text_by_name(driver, elem_name, msg):
	#element = driver.find_element_by_name("departureAirportCode:field_pctext")
	element = driver.find_element_by_name(elem_name)
	element.send_keys(msg)
	element.click()
	time.sleep(1)
    
def fill_text_by_tag(driver, tag_name, msg):
	#element = driver.find_element_by_name("departureAirportCode:field_pctext")
	element = driver.find_element_by_tag_name(tag_name)
	element.send_keys(msg)
	element.click()
	time.sleep(1)
    
def select_date(driver, elem_name, t_date):
	#element = driver.find_element_by_id("departureDate:field_pctext")
	element = driver.find_element_by_id(elem_name)
	element.click()
	time.sleep(5)
	all_tds = driver.find_elements_by_tag_name("td")
	for td in all_tds:
		print td.get_attribute("abbr")
		#if td.get_attribute("abbr") == "2016-12-16":
		if td.get_attribute("abbr") == t_date:
			td.click()
			break
	
driver = webdriver.Chrome('C:\Python27\chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://eflow.infortrend.com/Process/Process?fid=379&lid=6678543&act=todo');
time.sleep(5) # Let the user actually see something!

fill_text_by_name(driver, "UserName", "jerry.cheng")
fill_text_by_name(driver, "Password", "infor@135")
element = driver.find_element_by_tag_name("button")
element.click()
time.sleep(5)

fill_text_by_tag(driver, "textarea", "GS Project")
click_submit_by_id(driver, "ContentPlaceHolder1_UcSign1_btnSend")
'''
fill_text(driver, "departureAirportCode:field_pctext", "Hong Kong")
fill_text(driver, "arrivalAirportCode:field_pctext", "Fukuoka")	

select_date(driver, "departureDate:field_pctext", "2016-12-16")
select_date(driver, "returnDate:field_pctext", "2016-12-22")

element = driver.find_elements_by_tag_name("btnResearch")
element.click()
time.sleep(5)
'''