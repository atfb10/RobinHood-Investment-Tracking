'''
Author: Adam Forestier
Date: May 5, 2023
Description: func.py contains the logic behind the running of the application
'''
import functools, robin_stocks, smtplib

from credentials import (
    ROBINHODD_USERNAME,
    ROBINHOOD_PASSWORD
)

def send_timely_mail(connection: smtplib.SMTP, email: dict) -> None:
    '''
    argument: SMTP CONNECTION. EmailMessage() object
    returns: None
    Description: send_timely_mail sends an email with share purchase price and its current status at the time the function runs.
    It then kills the connection to the google server
    '''
    connection.send_message(email)
    connection.quit()
    return

def extract_data() -> dict:
    '''
    arguments: None
    returns: Dictionary of investmentment data
    description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
    '''
    robin_stocks.robinhood.login(ROBINHODD_USERNAME, ROBINHOOD_PASSWORD)
    return robin_stocks.robinhood.build_holdings()

def build_message(data: dict) -> str:
    '''
    arguments: data. Dicionary of investment data 
    returns: string that will be the email content
    description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
    '''
    investment_status_msg = ''



    return investment_status_msg