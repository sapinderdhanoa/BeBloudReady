import requests

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page)


# page.status_code
# page.content

from bs4 import BeautifulSoup
import bs4
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
list(soup.children)
[type(item) for item in list(soup.children)]
[bs4.element.Doctype, bs4.element.NavigableString, bs4.element.Tag]

# to print txt of sample web page
# html = list(soup.children)[2]
# list(html.children)
# body = list(html.children)[3]
# list(body.children)
# p = list(body.children)[1]
# print(p.get_text())

# alternative way to print page content of sample website
soup = BeautifulSoup(page.content, 'html.parser')
soup.find_all('p')
# print (soup.find_all('p')[0].get_text())

# code to web scarping from weather website
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)

img = tonight.find("img")
desc = img['title']
# print(desc)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
periods


short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(short_descs)
# print(temps)
# print(descs)

import pandas as pd
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
})
weather

# print(periods,end='' )
# print(short_descs, end='')
# print(temps, end='')
# print(descs, end='')

# print to csv file
# import pandas as pd

# dictionary of lists
# d = {'Description': [descs],'Day': [periods],'Brief': [short_descs],'Temperature': [temps]}


# creating dataframe from the above dictionary of lists
# dataFrame = pd.DataFrame(d)
# print(dataFrame)

# write dataFrame to SalesRecords CSV file
# dataFrame.to_csv("C:\\Users\\Sapinder\\web.csv")

# open writer with file name
import csv
file_name = "weather.csv"
#  set new line to be '' so that new rows append
f = csv.writer(open(file_name,'w',newline=''))
# write a new row as a header
f.writerow(['Day','Description','Temperature'])
# to write contents of rows
i = 0
while i < 9:
    period = periods[i]
    short_desc = short_descs[i]
    temp = temps[i]
    f.writerow([period, short_desc, temp])
    i = i+1
    
    if i == 9:
        print("The End")
        break









