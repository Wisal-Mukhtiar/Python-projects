import sqlite3

conn = sqlite3.connect("Library_database.sqlite3")

c = conn.cursor()

# books table
c.execute("""CREATE TABLE books(
    Name TEXT,
    Author TEXT,
    ISBN    INTEGER,
    Publishers TEXT,
    Book_id TEXT,
    copies_available INTEGER
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
    book1_id TEXT,
    book2_id TEXT,
    book3_id TEXT,
    book4_id TEXT,
    book5_id TEXT,
    book6_id TEXT,
    book7_id TEXT,
    book8_id TEXT,
    book9_id TEXT,
    book10_id TEXT,
    FOREIGN KEY(issued_member_id) REFERENCES member(member_id) ON DELETE SET NULL
)""")


conn.commit()

c.close()
