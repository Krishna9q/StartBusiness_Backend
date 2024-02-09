from icalendar import Calendar, Event
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from bs4 import BeautifulSoup
from pathlib import Path

import requests

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "sangeetatraders188@gmail.com"
smtp_password = "ctuvsymsarkuuumg"
from_email = "sangeetatraders188@gmail.com"

def send_verification_email(otp, user_email):
    html_content = ""

   

    message = MIMEMultipart("alternative")
    message["Subject"] = "Verification Email"
    message["From"] = from_email
    message["To"] = user_email
    to_email = user_email
    # Attach HTML content
    body = "this is your otp "+str(otp)
    message.attach(MIMEText(body, 'plain'))
  
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_email, to_email, message.as_string())
    server.quit()

