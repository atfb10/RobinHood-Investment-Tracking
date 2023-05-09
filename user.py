'''
Author: Adam Forestier
Date: May 5, 2023
Description: user contains the User class that stock data is gathered for
'''
import shutil as sh
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import robin_stocks
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from plotly.subplots import make_subplots

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
        self.__graph()
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
        df = pd.DataFrame(robin_stocks.robinhood.build_holdings()).transpose().reset_index().rename({'index': 'ticker'}, axis=1).drop('id', axis=1)
        df = df.astype({'ticker': 'category'}) 
        df = df.astype({'price': 'float64'}) 
        df = df.astype({'quantity': 'float64'}) 
        df = df.astype({'average_buy_price': 'float64'}) 
        df = df.astype({'equity': 'float64'}) 
        df = df.astype({'intraday_percent_change': 'float64'}) 
        df = df.astype({'type': 'category'}) 
        df = df.astype({'pe_ratio': 'float64'}) 
        df = df.astype({'percentage': 'float64'}) 
        return df

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
    
    def __graph(self) -> None:
        '''
        arguments: self
        returns: none
        description: function to call all private method graphing functions
        '''
        self.__equity_change_by_company()
        self.__percentage_holdings_by_company()
        return

    def __move_graph_to_user_folder(self, filename) -> None:
        '''
        arguments: self, name of file to move
        returns: none
        description: moves graph file to proper folder
        '''
        old_path = f'{PATH_TO_PROJECT}\\{filename}' 
        new_path = f'{self.directory}\\{filename}'
        if os.path.isfile(new_path):
            os.remove(new_path)
        os.rename(old_path, new_path)
        return

    def __equity_change_by_company(self) -> None:
        '''
        arguments: None
        returns: None
        description: Plotly bar graph of equity change by company
        '''
        df = self.df
        df = df.sort_values('equity_change')
        fig = px.histogram(df, x='name', y='equity_change', color='name', title='Equity Change by Company', text_auto=True)
        filename =  'Equity Change by Company.html'
        pyo.plot(fig, filename=filename)
        self.__move_graph_to_user_folder(filename)
        return
    
    def __percentage_holdings_by_company(self) -> None:
        '''
        arguments: self
        returns: None
        description: creates a plotly graph of the percentage of total holdings for each company
        '''
        df = self.df
        fig = px.pie(df, values='percentage', names='name', title='Percentage of Holdings by Company')
        filename = 'Percent Holdings by Company.html'
        pyo.plot(fig, filename=filename)
        self.__move_graph_to_user_folder(filename)
        return