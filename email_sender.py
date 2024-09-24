import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read.text())
email = EmailMessage()
email['from'] = 'Sender Name'
email['to'] = 'reciever.email@gmail.com'
email['subject'] = 'Sent through Python Script'

email.set_content(html.substritute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('sender.email@gmail.com', 'password')
	smtp.send_message(email)
	print('Successful')
