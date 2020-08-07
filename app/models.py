from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), index=True, unique=True)
    email = db.Column(db.String(200), index=True, unique=True)
    password_hash = db.Column(db.String(150))
    about_me = db.Column(db.String(300))
    nickname = db.Column(db.String(150))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    softwares = db.relationship('Software', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def set_password(self, senha):
        self.password_hash = generate_password_hash(senha)

    def check_password(self, senha):
        return check_password_hash(self.password_hash, senha)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode( {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    tag = db.Column(db.String(200), index=True)
    category = db.Column(db.String(200), index=True)
    sphere = db.Column(db.String(200), index=True)
    city = db.Column(db.String(200), index=True)
    state = db.Column(db.String(200), index=True)
    country = db.Column(db.String(200), index=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    similares = db.relationship('Similar', backref='post', lazy='dynamic')
    comments = db.relationship('Comment', backref='post', lazy='dynamic')
    reports = db.relationship('Report', backref='post', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)

    def as_dict(self):
        return {'title': self.title}


class Software(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    tag = db.Column(db.String(200), index=True)
    category = db.Column(db.String(200), index=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    license = db.Column(db.String(200), index=True)
    owner = db.Column(db.String(200), index=True)
    dateCreation = db.Column(db.String(200), index=True, default=datetime.utcnow)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    similares = db.relationship('Similar', backref='software', lazy='dynamic')
    comments = db.relationship('Comment', backref='software', lazy='dynamic')
    reports = db.relationship('Report', backref='software', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Software {}>'.format(self.title)

    def as_dict(self):
        return {'title': self.title}


class Similar(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Similar {}>'.format(self.name)


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    email = db.Column(db.String(200), index=True)
    text = db.Column(db.String(600), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Comment {}>'.format(self.name)


class Report(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    description = db.Column(db.String(500), index=True)
    type = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    software_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Report {}>'.format(self.name)
