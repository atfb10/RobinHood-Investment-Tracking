'''
Author: Adam Forestier
Date: March 12, 2023
Description: app.py manages the running of the application
'''

import smtplib
from email.message import EmailMessage

# Import variables
from credentials import (
    EMAIL_FROM,
    EMAIL_FROM_PASSWORD,
    EMAIL_TO
)
from func import (
    build_message,
    extract_data,
    send_timely_mail
)

# Connect to gmail
PORT = 587
HOST = 'smtp.gmail.com'
SMTP_CONNECTOR = smtplib.SMTP(host=HOST, port=PORT)
SMTP_CONNECTOR.starttls()
SMTP_CONNECTOR.login(EMAIL_FROM, EMAIL_FROM_PASSWORD)

investment_data = extract_data()
email_content = build_message(investment_data)

# generate email message
email = EmailMessage()
email['Subject'] = 'Investing Update'
email['From'] = EMAIL_FROM
email['To'] = EMAIL_TO
email.set_content(email_content)

# Send email when it is time
send_timely_mail(SMTP_CONNECTOR, email)