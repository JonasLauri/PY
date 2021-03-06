#!/usr/bin/env python3
# This script makes login automatically at letterboxd website
from selenium import webdriver
import sys, requests
url = "https://letterboxd.com/"

# Status code lookup
r = requests.get(url)
r.raise_for_status()

def auto_log(USER_NAME, USER_PASS):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath("//a[@class='navlink has-icon']").click()
    driver.find_element_by_id("username").send_keys(USER_NAME)
    driver.find_element_by_id("password").send_keys(USER_PASS)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    driver.close()

if __name__ == "__main__":
    USER_NAME = sys.argv[1]
    USER_PASS = sys.argv[2]
    auto_log(USER_NAME, USER_PASS)

