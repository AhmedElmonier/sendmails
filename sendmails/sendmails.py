import os
import smtplib
from email.message import EmailMessage

user = os.environ.get('IMPEX_EMAIL')
password = os.environ.get('IMPEX_PASS')


msg = EmailMessage()
msg['Subject'] = 'Hello There'
msg['From'] = user
msg['To'] = 'elmonierahmed@outlook.com'
msg.set_content('Hello There')

with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo
    smtp.login(user, password)
    smtp.send_message(msg)
    print('done!')
    smtp.close()







#sendto = 'elmonierahmed@outook.com'
#smtpsrv = "smtp.office365.com"
#smtpserver = smtplib.SMTP(smtpsrv,587)

#smtpserver.ehlo()
#smtpserver.starttls()
#smtpserver.ehlo
#smtpserver.login(user, password)
#msgbody = 'This is a test Email send using Python'
#smtpserver.sendmail(user, sendto, msgbody)
#print('done!')
#smtpserver.close()
