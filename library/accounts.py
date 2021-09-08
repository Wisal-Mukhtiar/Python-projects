"""GENERAL ACCOUNT, LIBRARIAN AND MEMEBER ACCOUNT ETC"""
import sqlite3

from books import Book

conn = sqlite3.connect("library_database.sqlite3")

c = conn.cursor()



class Account:
    """this is general account class, librarian and member will be inherited"""

    def __init__(self):
        self.name = None
        self.email = None
        self.phone = None
        self.password = None


class LibrarianAccount(Account):
    """The librarian account"""

    def __init__(self):
        super().__init__()
        librarian_id = None
        password = None

    def create_librarian_account(self):
        self.name = input("Enter your name : ")
        self.email = input("Enter your email address : ")
        self.phone = int(input("Enter your phone number : "))
        self.id = self._generate_librarian_id()


    def _generate_librarian_id(self):
        c.execute("""""")



class MemberAccount(Account):
    """The Member account"""

    def __init__(self):
        super().__init__()
        member_id = None
        password = None








