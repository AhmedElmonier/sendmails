import os
import csv
import smtplib
from email.message import EmailMessage
import pandas as pd



email = pd.read_csv('emails1.csv', delimiter=',')

print(email)
print(type(email))

user = os.environ.get('IMPEX_EMAIL')
password = os.environ.get('IMPEX_PASS')


msg = EmailMessage()
msg['Subject'] = 'Hello There'
msg['From'] = user
msg['To'] = email
msg.set_content('Hello There')


with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)
    smtp.send_message(msg)
    print('done!')
    smtp.close()
