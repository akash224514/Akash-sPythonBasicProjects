#Convert PDF File Text to Audio Speech using Python
'''
1)Import the PyPDF2 and pyttx3 modules.
2)Open the PDF file.
3)Use PdfFileReader() to read the PDF. We just have to give the path of the PDF as the argument.
4)Use the getPage() method to select the page to be read.
5)Extract the text from the page using extractText().
6)Instantiate a pyttx3 object.
7)Use the say() and runwait() methods to speak out the text.
'''

import PyPDF4
import pyttsx3

#Open a pdf as a file and extract data


with open('Resign_letter.pdf','rb') as f:
    pdf_reader=PyPDF4.PdfFileReader(f)  #creating a pdf file reader object
    a=pdf_reader.getNumPages()          #Getting number of pages of all document
    page=pdf_reader.getPage(0)          #get the page you want to read
    text=page.extractText()             #Extracting the text from pdf


print(f"\nNumber of pages are:{a}")     #printing number of pages
print(text)                             #Printing extracted data from pdf file


#Reading the text
r=pyttsx3.init()                        #Initializing the pyttx3 module object
voices=r.getProperty('voices')          #Setting a voice object
r.setProperty('voice',voices[0].id)     #Deciding for male or female voice
r.say(text)                             #Converted a text into speech
r.runAndWait()                          #Running a speech engine