"""module contain info about books of library"""


class Books:
    """Books class containing book information and stats"""

    def __init__(self, name, author_name, publisher, accession_number):
        self.name = name
        self.author_name = author_name
        self.publisher = publisher
        self.accession_number = accession_number

    def add_book(self):
        self.name = input("Enter book name : ")
        self.author_name = input("Enter author's name:  ")
        self.publisher = input("Enter publisher's name")

    def remove_book(self):
        remove_book_isbn = input("Enter isbn of the book: ")
        remove_book_accNum = input("Enter the acession number of the book to be removed : ")