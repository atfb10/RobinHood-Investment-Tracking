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
    EMAIL_TO,
    ROBINHODD_USERNAME,
    ROBINHOOD_PASSWORD
)
from user import RobinUser

def run_app() -> None:
    '''
    perform's running of the app. Allows schedule to work
    create user and call send email method for user
    '''
    user = RobinUser(username=ROBINHODD_USERNAME, password=ROBINHOOD_PASSWORD, email=EMAIL_TO)
    user.send_mail()

# TODO: Perform Functionality every market close on Fridays
while True:
    # schedule.every().friday.at('14:00', timezone('US/Mountain')).do(run_app())
    # schedule.every().friday.at('13:00').do(run_app)
    # schedule.every().minute.do(run_app)

# schedule.every().friday.at('14:00', timezone('US/Mountain')).do(run_app())