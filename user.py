'''
Author: Adam Forestier
Date: May 5, 2023
Description: user contains the User class that stock data is gathered for
'''
import shutil as sh
import os
import pandas as pd
import robin_stocks
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from credentials import (
    PATH_TO_PROJECT, 
    EMAIL_FROM, 
    EMAIL_FROM_PASSWORD
)

# Constants
PORT = 587
HOST = 'smtp.gmail.com'
EMAIL_SUBJECT = 'Weekly Stock Update'

class RobinUser:
    def __init__(self, username: str, password: str, email: str):
        '''
        RobinUser contructor
        '''
        self.username = username
        self.password = password
        self.email = email
        self.directory = f'{PATH_TO_PROJECT}\\user_files\\{username}'
        self.df = self.__extract_data()
        self.__zip_user_folder()

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
    
    def __extract_data(self) -> pd.DataFrame:
        '''
        arguments: None
        returns: Dictionary of investmentment data
        description: extract data gets the desired data from one's RobinHood account and returns it as a Pandas Dataframe
        '''
        robin_stocks.robinhood.login(username=self.username, password=self.password)
        return pd.DataFrame(robin_stocks.robinhood.build_holdings()).transpose().reset_index().rename({'index': 'ticker'}, axis=1)

    def __build_message(self) -> str:
        '''
        arguments: data. Dataframe of current holdings
        returns: string that will be the email content
        description: extract data gets the desired data from one's RobinHood account and returns it as a Python dictionary object
        '''
        equity_change_by_tick = self.df['equity_change'].to_list()
        equity_change = 0
        for ec in equity_change_by_tick:
            ec = float(ec)
            equity_change += ec
        equity_change = round(equity_change, 2)
        message = f'''Happy Friday!

        Your total Equity Change for current investments is ${equity_change}.

        Attached in the zipfile below is further details.
        
        Cheers,
        Adam
        '''
        return message
    
    def __zip_user_folder(self) -> None:
        '''
        arguments: self
        returns: None
        description: zip_user_folder creates a zip folder from a user folder for email
        '''
        # parent_dir = f{PATH_TO_PROJECT}''
        # user_folder = self.username
        # path = os.path.join(parent_dir, user_folder)
        sh.make_archive(f'{self.directory}', 'zip', self.directory)
        return
    
    def send_mail(self) -> None:
        '''
        arguments: self
        returns: None
        Description: send_email sends an email to user containing a zip file with all user data and graph files
        '''
        msg = MIMEMultipart()
        body_part = MIMEText(self.__build_message(), 'plain')
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