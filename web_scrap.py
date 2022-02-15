#Implementation of Web-Scraping using python (Extracting a title of a webpage)

import requests
import bs4

#Creating an object for making request to an URL
req_obj=requests.get('https://scrapy.org/')

#Creating an object for extracting a data
soup=bs4.BeautifulSoup(req_obj.text,'html.parser')

#From etracted data selecting a required data / filtering a required data
extr_data=soup.select('title')

#printing a final output as a required data
print(extr_data[0].get_text())