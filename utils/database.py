import sqlite3

conn = sqlite3.connect("database/resume.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS resume_history(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT,

email TEXT,

phone TEXT,

score INTEGER

)
""")

conn.commit()


def save_resume(name,email,phone,score):

    cursor.execute("""

    INSERT INTO resume_history(name,email,phone,score)

    VALUES(?,?,?,?)

    """,(name,email,phone,score))

    conn.commit()


def get_history():

    cursor.execute("SELECT * FROM resume_history")

    return cursor.fetchall()