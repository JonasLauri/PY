#!/usr/bin/env python3
#Scrape some data from internet and save csv file

from bs4 import BeautifulSoup
import requests as r
import csv
import os

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
html = r.get(url)
html.raise_for_status()


soup = BeautifulSoup(html.text, "lxml")
# Get gdp table with find()/find_all() methods
gdp_table = soup.find("table", {"class" : "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")


# Get gdp table headings
headings = []
for td in gdp_table_data[0].find_all("td"):
    headings.append(td.b.text.replace('\n', ' ').strip())
#print(headings)

# Get gdp table data sets
data = {}
for table, heading in zip(gdp_table_data[1].find_all("table"), headings):
    # Headers of table
    t_headers = []
    for th in table.find_all("th"):
        t_headers.append(th.text.replace('\n', ' ').strip())
    # All rows af table
    table_data = []
    for tr in table.tbody.find_all("tr"):
        # Each row has 3 cols
        t_row = {}
        # Find all td and zip with t_headers
        for td, th in zip(tr.find_all("td"), t_headers):
            t_row[th] = td.text.replace('\n', ' ').strip()
        table_data.append(t_row)
    # Data with his heading
    data[heading] = table_data


# Export data to csv
for topic, table in data.items():
    os.chdir('/Users/jonaslaurinaitis/Desktop/')
    with open(f"{topic}.csv", "w") as out_file:
        headers = [
            "Country/Territory",
            "GDP(US$million)",
            "Rank"
        ] #==t_headers
        writer = csv.DictWriter(out_file, headers)
        writer.writeheader()
        for row in table:
            if row:
                writer.writerow(row)
    
        
        
    

    


