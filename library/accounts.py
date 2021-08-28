""""user information via this module """
from enum import Enum


class AccountStatus(Enum):
    active, closed, cancel, blacklisted, NONE = 1, 2 , 3 , 4 ,5


class Account:
    """class contain all the info regarding user"""

    def __init__(self, name, email, password, account_status):
        self.name = name
        self.email = email
        self.password = password
        self.account_status = None

class Admin(Account):
    """administrator of the library may be more than one """

    def __init__(self, name, email, password, account_status= ):

        super().__init__(name, email, password,)





    def add_book(self):
