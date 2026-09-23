from models import User
import os
from database import init_db, DB_NAME
from pathlib import Path

def auth_cli():
    while True:
        print("[1]Criar um usuario\n[2]Logar com o usuario\n[3]Sair")
        print()

        try:
            choice = int(input("Opção: "))
        except:
            os.system("clear")
            print("Escolha uma opção válida")

        if choice == 1:
            os.system("clear")
            username = input("Digite um nome de usuario: ")
            email = input("Digite um email: ")
            password = input("Digite sua senha: ")
            confirm_password = input("Confirme sua senha: ")

            user = User(
                username=username,
                email=email,
                password=password,
                confirm_password=confirm_password,
            )
            user.create_user()

        elif choice == 2:
            email = input("Digite seu email: ")
            password = input("Digite sua senha: ")

            User.login_user(email, password)
        elif choice == 3:
            break
        else:
            print("Opção incorreta, tente novamente.")


if __name__ == "__main__":
    arquive = Path(DB_NAME)
    if not arquive.exists():
        init_db()

    auth_cli()