from flask import Flask, render_template

from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import PasswordField, StringField, TextAreaField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

from data import db_session
from data.users import User
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/Mars.sqlite")

    session = db_session.create_session()
    user_captain = User()
    user_captain.surname = 'Scott'
    user_captain.name = 'Ridley'
    user_captain.age = 21
    user_captain.position = 'captain'
    user_captain.speciality = 'research engineer'
    user_captain.address = 'module_1'
    user_captain.email = 'scott_chief@mars.org'
    session.add(user_captain)
    session.commit()

    app.run()


if __name__ == '__main__':
    main()
