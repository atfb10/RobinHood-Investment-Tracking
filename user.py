'''
Author: Adam Forestier
Date: May 5, 2023
Description: user contains the User class that stock data is gathered for
'''

class RobinUser:

    def __init__(self, username: str, password: str, email: str):
        '''
        every mountain project user has a userid and username
        '''
        self.username = username
        self.password = username
        self.email = email
        self.user_tick_url = f'{self.BASE_URL}{userid}/{username}{self.TICK}'
        self.user_tick_export_url = f'{self.BASE_URL}{userid}/{username}{self.TICK_EXPORT}'
        self.df = None

    def __repr__(self) -> str:
        '''
        prints the user's id and name 
        '''
        return f'Username: {self.username}. User Email: {self.email}'