'''
Author: Adam Forestier
Date: May 5, 2023
Description: user contains the User class that stock data is gathered for
'''

import pandas as pd

from credentials import PATH_TO_PROJECT

class RobinUser:

    def __init__(self, username: str, password: str, email: str, df: pd.DataFrame):
        '''
        every mountain project user has a userid and username
        '''
        self.username = username
        self.password = username
        self.email = email
        self.user_tick_url = f'{self.BASE_URL}{userid}/{username}{self.TICK}'
        self.directory = f'{PATH_TO_PROJECT}/user_files/{username}'
        self.df = df

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