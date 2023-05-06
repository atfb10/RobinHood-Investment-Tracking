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
    ROBINHODD_USERNAME,
    ROBINHOOD_PASSWORD
)
from user import RobinUser

def run_app() -> None:
    '''
    perform's running of the app. Allows schedule to work
    TODO: Put final project's functionality into here
    '''
    pass

# Create User
user = RobinUser(username=ROBINHODD_USERNAME, password=ROBINHOOD_PASSWORD, email=EMAIL_TO)
user.send_mail()

# TODO: Perform Functionality every market close on Fridays
# schedule.every().friday.at('14:00', timezone('US/Mountain')).do(run_app())