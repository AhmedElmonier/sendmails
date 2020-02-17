import os
import smtplib
from email.message import EmailMessage

email_address = os.environ.get('SM_USER')
password = os.environ.get('SM_PASS')

msg = EmailMessage()
msg['Subject'] = 'Hello There'
msg['From'] = email_address
msg['To'] = 'ahmedonea2016@gmail.com'
msg.set_content('Hello Beauty')

with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.send_message(msg)

