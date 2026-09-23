from datetime import datetime
from database import get_connection
from security import get_password_hash, verify_password
import os


class User:
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.created_at = datetime.now()
    @classmethod
    def _verify_user_exist(email):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT * FROM users WHERE email = ?
            """,
                (email,),
            )
            result = cursor.fetchone()

            if result is not None:
                return result
            return False

    def create_user(self):
        with get_connection() as conn:
            if self._verify_user_exist(self.email):
                print("Esse usuario já está cadastrado!")
                return False

            if self.password != self.confirm_password:
                print("As senhas não coincidem!")
                return False

            password_hash = get_password_hash(self.password)

            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO users (username, email, password, created_at)
                VALUES (?, ?, ?, ?)
            """,
                (self.username, self.email, password_hash, self.created_at.isoformat()),
            )
            conn.commit()
            os.system("clear")
            print("=====Usuario Criado com sucesso======")
            print()

    @classmethod
    def login_user(cls, email, password):
        result = cls._verify_user_exist(email)
        if result and verify_password(password, result[3]):
            os.system("clear")
            print(f"Bem vindo, {result[1]}!! Você está logado!!!")
            print()
            return True
        os.system("clear")
        print("Credenciais inválidas ou o usuario não existe.")
        return False
