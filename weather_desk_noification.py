#Get Live Weather Desktop Notifications Using Python

'''
1.Extract data form given URL.
2.Scrape the data with the help of requests and Beautiful Soup.
3.Convert that data into html code.
4.Find the required details and filter them.
5.Save the result in the String.
6.Pass the result in Notification object.
'''
#importing all dependence
from codecs import getdecoder
import requests
from bs4 import BeautifulSoup
import soupsieve
from win10toast import ToastNotifier

#Create an object for ToastNotifier
n=ToastNotifier()

#Define a fun for getting data from given URL
def getData(url):
    r=requests.get(url)
    return r.text

#Pass the URL to getData fun and convert that data into HTML
htmldata=getData("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")
soup=BeautifulSoup(htmldata,'html.parser')
print(soup.prettify()) #It enables us to view how the tags are nested in document

#Finding required details and filtering them
current_temp=soup.find_all("span", 
                             class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")

chances_rain=soup.find_all("div", 
                             class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp=(str(current_temp))
temp_rain=str(chances_rain)

result="current_temp"+ temp[128:-9]+" in Pune" +"\n"+temp_rain[131:-14]

#Pass the data into notification object
n.show_toast("weather update",result,duration=10)