#! /usr/bin/env python3
import bs4, requests
import pandas as pd 

url = 'https://forecast.weather.gov/MapClick.php?lon=-122.18576542823025&lat=37.87574002604113#.XrujLRMzY1I'
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text, 'html.parser')
seven_day = soup.find(id='seven-day-forecast')
forecast_items = seven_day.find_all(class_ = "tombstone-container")
#overnight = forecast_items[0]
#img = overnight.find('img')
#img_t = img['title']


# One data extracting way
img_titles = []
all_days = []
for days in forecast_items:
    all_days.append(days.text.replace("\n", " ").strip())
    for img in days:
        img = days.find('img')
        img_t = img['title']
    img_titles.append(img_t.strip())

all_data = {}
for day, title in zip(all_days, img_titles):
    all_data[day] = title

# Other way with pandas

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.text.strip() for pt in period_tags]

short_decs = [sh.text.strip() for sh in seven_day.select(".tombstone-container .short-desc")]
temp = [t.text.strip() for t in seven_day.select(".tombstone-container .temp")]
img = [img["title"] for img in seven_day.select(".tombstone-container img")]

table_data = pd.DataFrame({
    "period" : periods,
    "short_decs" : short_decs,
    "temp" : temp,
    "desc" : img
    })

# Or make csv file
table_data.to_csv('csv_file.csv', sep=";", index=False)


    
