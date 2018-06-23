
#! usr/bin/python3
"""
This program recieves the user's sender's and reiceiver's email address, 
the subject, message  and finally sends it .
"""

import smtplib
from email.mime.text import MIMEText as text

def sendEmail():
    try:

        receipient = input(" Insert the reciepient's email address >>").lower()

        print(" ")
        sender= input(" Insert the sender's email address >>").lower()
        print(" ")
        subject=input("What is the Email SUbject? >>")
        print(" ")
        message= input(" Compose your message here >>").capitalize()
        print(" ")

        m=text(message)
        m['Subject']= subject
        m['From']=sender
        m['To']=receipient

        server= smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("youremail@gmail.com","xxxxxx")
        

        server.sendmail(sender,receipient, m.as_string())
        server.quit()


        print ("Email Successfully Sent")
    except:
        print ("Email Not Sent")




sendEmail()