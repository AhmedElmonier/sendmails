import os
from string import Template
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


file = pd.read_csv('emails.csv', delimiter=',', encoding= 'unicode_escape')
emails = list(file['Email'])

print(len(emails))
        
user = os.environ.get('IMPEX_EMAIL')
password = os.environ.get('IMPEX_PASS')


def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

message_template = read_template('msg_impex.txt')
message = message_template.substitute()


with smtplib.SMTP('smtp.office365.com', 587) as smtp:
    smtp.starttls()
    smtp.login(user, password)
    count = 1
    for email in emails:
        msg = MIMEMultipart()       # create a message

        # Prints out the message body for our sake
        print(message)

        print(count)
        count = count +1
        print("Sending email to", email)

        # setup the parameters of the message
        msg['From']= user
        msg['To']= email
        msg['Subject']= "The Supplier Your Company Has Always Needed"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        print(type(msg))
        smtp.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    smtp.quit()
