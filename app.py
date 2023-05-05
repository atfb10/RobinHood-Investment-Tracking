'''
Author: Adam Forestier
Date: May 5, 2023
Description: app.py manages the running of the application
'''
import schedule

from pytz import timezone

from email.message import EmailMessage

# Import variables
from credentials import (
    EMAIL_FROM,
    EMAIL_FROM_PASSWORD,
    EMAIL_TO,
    PHONE_NUM,
)
from func import (
    build_message,
    extract_data
)

# Connect to gmail
# PORT = 587
# HOST = 'smtp.gmail.com'
# SMTP_CONNECTOR = smtplib.SMTP(host=HOST, port=PORT)
# SMTP_CONNECTOR.starttls()
# SMTP_CONNECTOR.login(EMAIL_FROM, EMAIL_FROM_PASSWORD)

# Get Data
investment_data = extract_data()
print(investment_data)

# Generate text message
text_msg = build_message(investment_data)



# TODO: Perform Functionality every 5 minutes during week when stock market is open
# schedule.every().monday.at('7:30', timezone('US/Mountain')).do(send_timely_mail(SMTP_CONNECTOR, email))
# schedule.every().friday.at('14:00', timezone('US/Mountain')).do(send_timely_mail(SMTP_CONNECTOR, email))
