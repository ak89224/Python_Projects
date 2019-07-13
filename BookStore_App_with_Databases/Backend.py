import sqlite3


def connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books(id integer PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def insert(title, author, year, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()


#connect()
#insert("The Sun", "Jhon RAA", 2013, 12345623743)
#print(view())
#update(1, "The Moon", "Jhon Smooth", 2003, 72292428924)
#print(view())
#print(search(author="Jhon Mobile"))
#delete(9)
#print(view())