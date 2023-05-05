'''
Author: Adam Forestier
Date: May 5, 2023
Description: func.py contains the logic behind the running of the application
'''
import pandas as pd
import functools, robin_stocks

def extract_data(username: str, password: str) -> pd.DataFrame:
    '''
    arguments: None
    returns: Dictionary of investmentment data
    description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
    '''
    robin_stocks.robinhood.login(username=username, password=password)
    return pd.DataFrame(robin_stocks.robinhood.build_holdings()).transpose().reset_index().rename({'index': 'ticker'}, axis=1)

def build_message(df: pd.DataFrame) -> str:
    '''
    arguments: data. Dataframe of current holdings
    returns: string that will be the email content
    description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
    '''
    ticker = df.iloc[0]['ticker']
    equity_change = df.iloc[0]['equity_change']
    investment_status_msg = f'Your current equity change for {ticker} = ${equity_change}'

    return investment_status_msg

