from flask import render_template, url_for, flash, redirect
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, SignupForm, AddNoteForm

from . import app, lm
from models import user, note

@lm.user_loader
def load_user(user_id):
    return user.query.filter_by().first()

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
        if userName is not None and userName.check_password(form.password.data):
            login_user(userName, form.remember_me.data)
            flash("Login successful.")
            return redirect(url_for('home'))
        else:
            flash("Login failed.")
    return render_template('login.html', form = form)

@login_required
@app.route('/home')
def home():
    notes = note.query.filter_by(userid = current_user.userid)
    return render_template('home.html', notes = notes)

@login_required
@app.route('/add', methods = ['GET', 'POST'])
def add():
    form = AddNoteForm()
    Notes = note.query.filter_by(userid=current_user.userid).first()
    if form.validate_on_submit():
        new = note(title=form.title.data, content=form.content.data, userid=current_user.userid)
        new.save()
        flash('Note created successfully')
        return redirect(url_for('home'))
    return render_template('new.html', form = form, Notes = Notes)

@login_required
@app.route('/view/<id>')
def view(id):
    notes = note.query.get(id)
    Notes = note.query.filter_by(userid = current_user.userid).all()
    return render_template('note.html', note = notes, Notes = Notes)

@login_required
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))