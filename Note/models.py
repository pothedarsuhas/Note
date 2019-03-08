from datetime import datetime
from hashlib import md5

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from Note import db  #C:\Users\1338826\PycharmProjects\IC2\Note\Note\note.db

class user(db.Model, UserMixin):
    '''
    id number
    username string
    email string
    '''
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120))
    email = db.Column(db.String(120), unique=True, nullable=False)
    note = db.relationship('note', backref= 'user', lazy = 'dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def get_id(self, id):
    #     return self.id

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_by_email(email):
        return user.query.filter_by(email=email).first()

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def get_id(self):
        return (self.userid)


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
    userid = db.Column(db.Integer, db.ForeignKey(user.userid))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, title, content, userid):
        self.title = title
        self.content = content
        self.userid = userid

db.create_all()