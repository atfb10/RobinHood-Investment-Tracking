'''
Author: Adam Forestier
Date: May 5, 2023
Description: func.py contains the logic behind the running of the application
'''
import pandas as pd
import functools, robin_stocks

from credentials import (
    ROBINHODD_USERNAME,
    ROBINHOOD_PASSWORD
)

def extract_data() -> dict:
    '''
    arguments: None
    returns: Dictionary of investmentment data
    description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
    '''
    robin_stocks.robinhood.login(ROBINHODD_USERNAME, ROBINHOOD_PASSWORD)
    return pd.DataFrame(robin_stocks.robinhood.build_holdings()).transpose().reset_index().rename({'index': 'ticker'}, axis=1)

def build_message(data: dict) -> str:
    '''
    arguments: data. Dicionary of investment data 
    returns: string that will be the email content
    description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
    '''
    investment_status_msg = ''



    return investment_status_msg