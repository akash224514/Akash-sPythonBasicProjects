#Scraping One Plus India's 2022 Phone's List
'''Idea -   Scrap a data for any specific product on amazon and analyze its customer reviews.
            Do sentiment analysis and perform necessary statistical analysis '''


from cgitb import text
from bs4 import BeautifulSoup as bs
import requests
import bs4

#Accessing the WebPage using request module
link="https://www.oneplus.in/store/phone"
page= requests.get(link)

#Get the Parsed HTML code/Tags of required site
soup=bs4.BeautifulSoup(page.content,'html.parser')

#Printing whole HTML Document if needed
#print(soup.prettify())



#We w'll look towards phone's list section
testmon=soup.find_all('dl')

#Printing phone's list using get_text()
print(testmon[0].get_text()) 
