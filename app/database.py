import sqlite3

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

try:
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
            created_at DATE NOT NULL
        );
    """)

    conn.close()
    print("O banco foi criado com sucesso.")
except sqlite3.OperationalError:
    print("O banco já foi criado.")
