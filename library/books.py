"""books class contain all the information related to books"""
import sqlite3

conn = sqlite3.connect("library_database.sqlite3")

c = conn.cursor()

class Book:
    """Book class"""

    def __init__(self):
        self.name = None
        self.authors = None
        self.ISBN = None
        self.publishers = None
        self.accesion_number = None
        
    def add_book(self):
        self.name = input("Enter the book name : ")
        self.authors = input("Enter the names of the author with comma and space : ")
        self.ISBN = int(input("Enter the ISBN of the book : "))
        self.publishers = input("Enter the names of the publishers : ")
        quantity = int(input("Enter the quantity of books : "))
        accession_number = self._retrieve_accession()
        self._save_book_record(accession_number, quantity)

        self._store_books(accession_number,quantity)


    def _save_book_record(self, accession_number, quantity):
        c.execute(f"""INSERT INTO books
        VALUES(?,?,?,?,?,?)""",(self.name, self.authors, self.ISBN,
                                self.publishers, accession_number, quantity))

    def _store_books(self, accession_number, quantity):
        for i in range(quantity):
            current_accession = str(accession_number) + ":"+str(i+1)
            c.execute("""INSERT INTO books_storage
            VALUES(?,?,?,?,?)""",(self.name, self.authors, self.ISBN,
                                self.publishers, current_accession))

            conn.commit()

    def _retrieve_accession(self):
        c.execute("""SELECT Accession_number FROM books
              WHERE ROWID = ( SELECT max( ROWID ) FROM books)""")
        accession_number = c.fetchall()
        print(accession_number)
        if accession_number:
            return accession_number[0][0] + 1
        else:
            return 0


b = Book()
b.add_book()







