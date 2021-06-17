import sqlite3

# we need some variable to connect to our database
# following line of code creates a database called library
conn = sqlite3.connect('library.db')

# create a cursor
cursor = conn.cursor()


# create a table
# Available data types for sqlite: NULL, INTEGER, REAL, TEXT, BLOB
create_library_table = """
CREATE TABLE IF NOT EXISTS library (
  isbn INTEGER PRIMARY KEY,
  author TEXT NOT NULL,
  title TEXT NOT NULL,
  year INTEGER,
  owner TEXT,
  current holder TEXT
  
);
"""


cursor.execute(create_library_table)
#--------------------------------------
# populating function, must be called after web scraper and user fill prompt are done working
def new_book(ISBN, title, author, year, owner):
    cursor.execute("INSERT INTO library VALUES (?,?,?,?,?,?)", ISBN, title, author, year, owner, owner)

#--------------------------------------
cursor.execute('SELECT * FROM library')
items = cursor.fetchall()

for item in items:
    print(item)

# commit our command
conn.commit();

# close our connection

conn.close();
