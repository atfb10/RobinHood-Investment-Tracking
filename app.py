'''
Author: Adam Forestier
Date: May 5, 2023
Description: app.py manages the running of the application
'''

# Libraries and Modules
import schedule

from pytz import timezone
from email.message import EmailMessage

# Local Imports
from credentials import (
    EMAIL_FROM,
    EMAIL_FROM_PASSWORD,
    EMAIL_TO,
    PHONE_NUM,
    ROBINHODD_USERNAME,
    ROBINHOOD_PASSWORD
)
from func import (
    build_message,
    extract_data,
    send_text
)

# Get Data
investment_data = extract_data(username=ROBINHODD_USERNAME, password=ROBINHOOD_PASSWORD)

# Generate text message
msg = build_message(df=investment_data)


# TODO: Perform Functionality every market close on Fridays
# schedule.every().friday.at('14:00', timezone('US/Mountain')).do(send_timely_mail(SMTP_CONNECTOR, email))
