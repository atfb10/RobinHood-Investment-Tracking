'''
Author: Adam Forestier
Date: May 5, 2023
Description: user contains the User class that stock data is gathered for
'''
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import pandas as pd
import robin_stocks

from credentials import (
    PATH_TO_PROJECT, 
    EMAIL_FROM, 
    EMAIL_FROM_PASSWORD
)

# Constants
PORT = 587
HOST = 'smtp.gmail.com'
EMAIL_SUBJECT = 'Weekly Stock Update'
MESSAGE_BODY = '''Howdy!

Attached is your weekly stock update

Best,
Adam
'''

class RobinUser:
    def __init__(self, username: str, password: str, email: str):
        '''
        RobinUser contructor
        '''
        self.username = username
        self.password = username
        self.email = email
        self.directory = f'{PATH_TO_PROJECT}\\user_files\\{username}'
        self.df = self.extract_data()

    def __repr__(self) -> str:
        '''
        prints the user's id and name 
        '''
        return f'Username: {self.username}. User Email: {self.email}'
    
    def __str__(self) -> str:
        '''
        prints the user's id and name 
        '''
        return f'Username: {self.username}. User Email: {self.email}'
    
    def extract_data(self) -> pd.DataFrame:
        '''
        arguments: None
        returns: Dictionary of investmentment data
        description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
        '''
        robin_stocks.robinhood.login(username=self.username, password=self.password)
        return pd.DataFrame(robin_stocks.robinhood.build_holdings()).transpose().reset_index().rename({'index': 'ticker'}, axis=1)

    def build_message(self) -> str:
        '''
        arguments: data. Dataframe of current holdings
        returns: string that will be the email content
        description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
        '''
        ticker = self.df.iloc[0]['ticker']
        equity_change = self.df.iloc[0]['equity_change']
        investment_status_msg = f'Your current equity change for {ticker} = ${equity_change}'

        return investment_status_msg
    
    def send_mail(self) -> None:
        '''
        arguments: self
        returns: None
        Description: send_email sends an email to user containing a zip file with all user data and graph files
        '''
        msg = MIMEMultipart()
        body_part = MIMEText(MESSAGE_BODY, 'plain')
        msg['Subject'] = EMAIL_SUBJECT
        msg['From'] = EMAIL_FROM
        msg['To'] = self.email
        msg.attach(body_part)
        parent_dir = 'user_files/'
        user_folder = str(self.username)
        path = os.path.join(parent_dir, user_folder)
        zip_path = f'{path}.zip'
        with open(zip_path,'rb') as file:
            msg.attach(MIMEApplication(file.read(), Name=zip_path))

        smtp_obj = smtplib.SMTP(host=HOST, port=PORT)
        smtp_obj.starttls()
        smtp_obj.login(EMAIL_FROM, EMAIL_FROM_PASSWORD)

        smtp_obj.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp_obj.quit()
        return