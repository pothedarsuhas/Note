from datetime import datetime
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from Note import db

class user(db.Model, UserMixin):
    '''
    id number
    username string
    email string
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    note = db.relationship('note', backref= 'user', lazy = 'dynamic')

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get_by_email(email):
        return user.query.filter_by(email=email).first()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)


class note(db.Model):
    '''
    id number
    title string
    content string
    last_modified date
    '''
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    content = db.Column(db.Text)
    last_modified = db.Column(db.Date)
    userid = db.Column(db.Integer, db.ForeignKey(user.id))

    def save(self):
        db.session.add()
        db.session.commit()

    def __init__(self, title, content, last_modified, userid):
        self.title = title
        self.content = content
        self.last_modified = last_modified
        self.userid = userid

