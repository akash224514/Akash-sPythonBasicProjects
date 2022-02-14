
#Importing the necessary module
from plyer import notification
import time

#specifying parameters
title='Hello Akash!'

message='You did enough work..Take a break and breath buddy!'

#Always executes loop while its true
while True:

    notification.notify(title=title,message=message,app_icon=None,timeout=10,toast=False)

    time.sleep(60*60) 