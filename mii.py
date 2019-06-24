
import smtplib

sender = 'ipsa77390@gmail.com'
receivers = ['ipsa77390@gmail.com']

message = """From: From Person <ipsa77390@gmail.com>
To: To Person <ipsa77390@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")