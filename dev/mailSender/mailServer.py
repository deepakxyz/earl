
import os
import smtplib
import imghdr
from email.message import EmailMessage


from aishoResume import msgContent

EMAIL_ADDRESS = 'grey.notificationsender@gmail.com'
EMAIL_PASSWORD = 'yepzqixrrdyifimn'

contacts = ['deepak.blackandwhite@gmail.com']

try:
    msg = EmailMessage()
    msg['Subject'] = 'Aishwarya Varadharaj'
    msg['From'] = f"Grey Notification<{EMAIL_ADDRESS}>"
    msg['To'] = ','.join(contacts)
    content = ''' Deepka ===== rajan '''
    msg.set_content(content)

    msg.add_alternative(msgContent,  subtype='html')
    


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

except:
    print('Problem in connecting to the server!')

