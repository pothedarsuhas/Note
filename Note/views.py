from flask import Flask, render_template, url_for
from flask_login import current_user, login_required

from . import app, lm
from .models import user, note

@lm.user_loader
def load_user(user_id):
    return user.get(user_id)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@login_required
@app.route('/home')
def home():
    return render_template('home.html')

@login_required
@app.route('/add')
def add():
    return render_template('new.html')

@login_required
@app.route('/view')
def view():
    return render_template('note.html')
