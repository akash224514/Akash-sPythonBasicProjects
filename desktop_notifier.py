
#Importing the necessary module
from plyer import notification

#specifying parameters
title='Hello Akash!'

message='This is your first desktop notification..'

notification.notify(title=title,message=message,app_icon=None,timeout=20,toast=False)
