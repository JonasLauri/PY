#!/usr/bin/env python3
# Auto login and scrape some data in letterboxd 
from selenium import webdriver
import config
driver = webdriver.Chrome()

def auto_log():
    
    driver.get("https://letterboxd.com/")
    driver.find_element_by_xpath("//a[@class='navlink has-icon']").click()
    driver.find_element_by_id("username").send_keys(config.USER_NAME)
    driver.find_element_by_id("password").send_keys(config.USER_PASS)
    driver.find_element_by_xpath("//input[@type='submit']").click()
