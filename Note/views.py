from flask import render_template, url_for, flash, redirect
from flask_login import login_required, login_user
from .forms import LoginForm, SignupForm, AddNoteForm

from . import app, lm
from .models import user, note

from . import app, lm
from .models import user, note

@lm.user_loader
def load_user(user_id):
    return user.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new = user(username = form.username.data, email = form.email.data, password = form.password.data)
        new.save()
        flash("Registration was successful")
        return redirect(url_for('login'))
    return render_template('signup.html', form = form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        userName = user.get_by_email(form.email.data)
        if userName is not None and user.check_password(form.password.data):
            login_user(userName, form.remember_me.data)
            flash("Login successful.")
            return redirect(url_for('home'))
        else:
            flash("Login failed.")
    return render_template('login.html', form = form)

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
