from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\1338826\\PycharmProjects\\IC2\\Note\\Note\\note.db'
db = SQLAlchemy(app)


db.create_all()


