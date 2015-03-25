__author__ = 'bernardo'


import csv
import mechanize
import re
import time
import BeautifulSoup
import smtplib

def sendEmail(result, sender, senderPwd, recipient = None):
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    if recipient == None:
        recipient = sender

    subject = 'ToA'
    body = result

    body = "<b>" + body + "<b>"

    headers = ["From: " + sender,
               "Subject: " + subject,
               "To: " + recipient,
               "MIME-Version: 1.0",
               "Content-Type: text/html"]
    headers = "\r\n".join(headers)

    session = smtplib.SMTP(SMTP_SERVER , SMTP_PORT)

    session.ehlo()
    session.starttls()
    session.ehlo
    session.login(sender, senderPwd)

    session.sendmail(sender, recipient, headers + "\r\n\r\n" + body)
    session.quit()

def haha():
	pass