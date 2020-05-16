from selenium import webdriver
import csv

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

browser = webdriver.Chrome()

# Store pages data in dict
users_data = {}
for i in range(1, MAX_PAGE_NUM + 1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"
    browser.get(url)
    
    names = browser.find_elements_by_xpath("//div[@title='buyer-name']")
    prices = browser.find_elements_by_css_selector(".item-price")

    for name, price in zip(names, prices):
        users_data[name.text] = price.text

browser.close()

# Store users_data in csv file
with open("users_data.csv", "w") as out_file:
    writer = csv.writer(out_file, delimiter = ";")
    writer.writerow(['Name', 'Price'])
    for row in users_data.items():
        writer.writerow(row)

