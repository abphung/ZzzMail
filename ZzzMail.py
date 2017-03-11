# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
import time

sg = sendgrid.SendGridAPIClient(apikey="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")
from_email = Email("phung8128@gmail.com")
to_email = Email("phung8128@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

import contextio as c

CONSUMER_KEY = 'gsfwxksk'
CONSUMER_SECRET = '6jvtq2M77vpLK5mY'
API_VERSION = 'lite' # "lite" or "2.0"

context_io = c.ContextIO(
  consumer_key=CONSUMER_KEY,
  consumer_secret=CONSUMER_SECRET,
  api_version=API_VERSION
)

accounts = context_io.get_users()
if accounts:
    account = accounts[0]

params = {
    'label': 0
}

EA = c.EmailAccount(account, params)

read = []
for message in EA.get_folders()[0].get_messages():
	try:
		read.append(message.get_flags()['flags']['read'])
	except:
		pass
print read
count = 0
while True:
	#every day after work at 8:00 pm get emails
	if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 0:
		read = []
		for message in EA.get_folders()[0].get_messages():
			try:
				read.append(message.get_flags()['flags']['read'])
			except:
				pass
		print read
	#every day at 4:00 am get emails
	if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 0:
		read2 = []
		for message in EA.get_folders()[0].get_messages():
			try:
				read.append(message.get_flags()['flags']['read'])
			except:
				pass
		print read2
		#compare the email data. If we detect an email was read increment count
		if sum(read) < sum(read2):
			count += 1
	#every week send weekly email
	if datetime.datetime.now().day == 0:
		sg = sendgrid.SendGridAPIClient(apikey="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")
		from_email = Email("phung8128@gmail.com")
		to_email = Email("phung8128@gmail.com")
		subject = "Sending with SendGrid is Fun"
		#this line is the body of the email
		content = Content("text/plain", "you've read" str(count) + "emails after hours this week")
		count = 0
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())