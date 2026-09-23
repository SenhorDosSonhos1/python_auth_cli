import pytest
import sqlite3
from app.database import sql

def get_connection():
    return sqlite3.connect(":memory:")


@pytest.fixture
def database():
    with get_connection() as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(sql)
            return conn
        
        except sqlite3.OperationalError as e:
            print("Erro ao inicializar o banco", e)



def test_database(database):
    ...