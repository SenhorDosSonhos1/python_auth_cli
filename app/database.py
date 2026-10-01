import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
sql = """
        CREATE TABLE users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at DATE NOT NULL
        );
        """

def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(sql)
            print("O banco foi criado/verificado com sucesso.")
        except sqlite3.OperationalError as e:
            print("Erro ao inicializar o banco", e)



