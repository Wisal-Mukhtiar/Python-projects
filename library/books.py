"""The books in the management system are represented via this module"""


class Books:
    """All the operations of library class"""

    def __init__(self, name, isbn, author, publishers):
        self.name = name
        self.isbn = isbn
        self.author = author
        self.publishers = publishers
        self.accession_number = None  # unique number assigned to each book for record track
