import os
import venv
from virtualenv import cli_run

with open("run.py", "w") as file:
    pass

cli_run(["venv"])

os.mkdir("app")
os.chdir("app")


with open("__init__.py", "w") as file:
    text = """from flask import Flask

app = Flask(__name__)"""
    file.write(text)

with open("models.py", "w") as file:
    pass

with open("config.py", "w") as file:
    text = """class Config:
    SECRET_KEY = "12345"
"""

    file.write(text)

def main():
    pass

if __name__ == "__main__":
    main()