
import os
import smtplib
import imghdr
from email.message import EmailMessage
from os.path import abspath, exists
import csv

from emailInfo import  E_SUBJECT, PORTFOLIO_LINK

E_ADDRESS = 'aishwarya.varadharaj@gmail.com'
E_PASSWORD = 'wxbkijshwbqlylhs'

f_path = abspath("resumeFinal.html")

if exists(f_path):
    with open(f_path) as f:
        
        html = f.read()
        msgContent = f'''{html}'''
        contentBody = msgContent.replace('PORTFOLIO_LINK',PORTFOLIO_LINK)
        
       

with open('emailAddress.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        
        msg = EmailMessage()
        msg['Subject'] = E_SUBJECT
        msg['From'] = f"Aishwarya Varadharaj<{E_ADDRESS}>"
        msg['To'] = ','.join(line)
        

        msg.add_alternative(contentBody,  subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(E_ADDRESS, E_PASSWORD)
            smtp.send_message(msg)
            
        print('email sent to',line[0])
    
