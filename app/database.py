import sqlite3

DB_NAME = "users.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
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
            print("O banco foi criado/verificado com sucesso.")
        except sqlite3.OperationalError as e:
            print("Erro ao inicializar o banco", e)
