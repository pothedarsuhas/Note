import os

from flask import url_for, render_template, Flask, views
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

lm = LoginManager()

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\1338826\\PycharmProjects\\IC2\\Note\\Note\\note.db'
app.config['SECRET_KEY'] = 'SECRET'
db = SQLAlchemy(app)

lm.init_app(app)
lm.session_protection = 'strong'
lm.login_view = "login"

from .views import *