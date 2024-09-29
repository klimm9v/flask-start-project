import os
from virtualenv import cli_run


def create_venv() -> None:

    with open("run.py", "w") as file:
        pass

    with open("README.md", "w") as file:
        pass

    cli_run(["venv"])


def create_files() -> None:
    with open("__init__.py", "w") as file:
        text = """from flask import Flask

app = Flask(__name__)"""
        file.write(text)
        file.close()

    with open("models.py", "w") as file:
        file.write("#create models in this file")
        file.close()

    with open("config.py", "w") as file:
        text = """class Config:
    SECRET_KEY = "12345"
    """

        file.write(text)
        file.close()


def create_dirs() -> None:
    os.mkdir("templates")
    os.mkdir("static")


def main():
    while True:
        name_project = input("Please give this project a title: ")
        if name_project:
            break

    os.mkdir(name_project)
    os.chdir(name_project)
    create_venv()
    os.mkdir("app")
    os.chdir("app")
    create_files()
    create_dirs()

if __name__ == "__main__":
    main()