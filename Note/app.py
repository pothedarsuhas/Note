from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

import os

# basedir = os.path.abspath(os.path.dirname(__file__))

db.create_all()
