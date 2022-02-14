#Send an Email using python
'''
1)Initiate the server
2)Authenticate the user --> Use login()
3)Give all necessary email parameters -->use sendmail()
4)Send an actual mail-->use sendmail()
5)Terminate the session between client and server -->use quit()

'''


from http import server
import smtplib,ssl
from email.message import EmailMessage

#Email parameters
mail_from="akashshelkande@gmail.com"
mail_To="akashshelkande08@gmail.com"
mail_body="Hi this akash from other side..mail test3"


server=smtplib.SMTP_SSL("smtp.gmail.com",465)                   #Naming a server
server.login("akashshelkande@gmail.com","@Akashmgv08")          #Log in essentials to authenticate the user
server.sendmail(mail_from,mail_To,mail_body)                    #send actual email 
print("\n Email sent successfully!")                            #Confirmation message
server.quit()                                                   #Terminate the session between client and SMTP server