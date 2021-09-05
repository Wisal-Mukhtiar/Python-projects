import sqlite3

conn = sqlite3.connect("Library_database.sqlite3")

c = conn.cursor()

# books table
c.execute("""CREATE TABLE books(
    Name TEXT,
    Author TEXT,
    ISBN    INTEGER,
    Publishers TEXT,
    Accession_number INTEGER,
    copies_available INTEGER
)""")

c.execute("""CREATE TABLE books_storage(
    Name TEXT,
    Author TEXT,
    ISBN    INTEGER,
    Publishers TEXT,
    Accession_id TEXT,
    FOREIGN KEY(ISBN) REFERENCES books(ISBN) ON DELETE SET NULL 
)""")
        


# librarian account table
c.execute("""CREATE TABLE librarian(
    name TEXT,
    email TEXT,
    librarian_id TEXT,
    passowrd TEXT,
    phone   INTEGER
)""")

# MEMBER ACCOUNT table
c.execute("""CREATE TABLE member(
    name TEXT,
    email TEXT,
    member_id TEXT,
    passowrd TEXT,
    phone   INTEGER,
    registered_by TEXT,
    FOREIGN KEY(registered_by) 
    REFERENCES librarian(librarian_id) ON DELETE SET NULL
)""")


# ISSUED BOOKS TABLE
c.execute("""CREATE TABLE issued_books(
    issued_member_id TEXT,
    book1_accession_number TEXT,
    book2_accession_number TEXT,
    book3_accession_number TEXT,
    book4_accession_number TEXT,
    book5_accession_number TEXT,
    book6_accession_number TEXT,
    book7_accession_number TEXT,
    book8_accession_number TEXT,
    book9_accession_number TEXT,
    book10_accession_number TEXT,
    FOREIGN KEY(issued_member_id) REFERENCES member(member_id) ON DELETE SET NULL
)""")


conn.commit()

c.close()
