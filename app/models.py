from datetime import datetime
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from app import db, login


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


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

    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def follow(self, user):
        if not self.is_following(user):
        	self.followed.append(user)

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)

    def is_following(self, user):
        return self.followed.filter(
        	followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                    followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    def followed_softwares(self):
        followed = Software.query.join(
            followers, (followers.c.followed_id == Software.user_id)).filter(
                followers.c.followed_id == self.id)
        own = Software.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Software.timestamp.desc())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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


favorites_post = db.Table('favorites_post',
    db.Column('favorite_id', db.Integer, db.ForeignKey('post.id'))
)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    sphere = db.Column(db.String(200), index=True)
    description = db.Column(db.String(800), index=True)
    officialLink = db.Column(db.String(300), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    similar = db.relationship('Similar', backref='similar_post', lazy='dynamic')
    tag = db.relationship('Tag', backref='tag_post', lazy='dynamic')
    category = db.relationship('Category', backref='category_post', lazy='dynamic')
    comment = db.relationship('Comment', backref='comment_post', lazy='dynamic')
    report = db.relationship('Report', backref='report_post', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
    	return '<Post {}>'.format(self.title)

    def as_dict(self):
        return {'title': self.title}

    def favorite(self, post):
        if not self.is_favorite(post):
        	self.favored.append(post)

    def unfavorite(self, post):
        if self.is_favorite(post):
            self.favored.remove(post)

    def is_favorite(self, post):
        return self.favored.filter(
        	favorites_post.c.favorite_id == post.id).count() > 0

    def favorite_posts(self):
        favored = Post.query.join(
            favorites, (favorites.c.favorite_id == Post.user_id)).filter(
                    favorites.c.favorite_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return favored.union(own).order_by(Post.timestamp.desc())


favorites_software = db.Table('favorites_software',
    db.Column('favorite_id', db.Integer, db.ForeignKey('software.id'))
)


class Software(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), index=True, unique=True)
    description = db.Column(db.String(800), index=True)
    downloadLink = db.Column(db.String(300), index=True)
    activeDevelopment = db.Column(db.String(200), index=True)
    license = db.Column(db.String(200), index=True)
    owner = db.Column(db.String(200), index=True)
    dateCreation = db.Column(db.String(300), index=True)
    dateRelease = db.Column(db.String(300), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    similar = db.relationship('Similar', backref='similar_software', lazy='dynamic')
    tag = db.relationship('Tag', backref='tag_software', lazy='dynamic')
    category = db.relationship('Category', backref='category_software', lazy='dynamic')
    comment = db.relationship('Comment', backref='comment_software', lazy='dynamic')
    report = db.relationship('Report', backref='report_software', lazy='dynamic')

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Software {}>'.format(self.title)

    def as_dict(self):
        return {'title': self.title}

    def avatar(self, size):
        digest = md5(self.title.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


class Similar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    postSimilar_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    softwareSimilar_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Similar {}>'.format(self.name)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    postTag_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    softwareTag_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Tag{}>'.format(self.tag)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    postCategory_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    softwareCategory_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Category {}>'.format(self.category)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    email = db.Column(db.String(200), index=True)
    text = db.Column(db.String(600), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    postComment_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    softwareComment_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Comment {}>'.format(self.name)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), index=True)
    description = db.Column(db.String(500), index=True)
    type = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    postReport_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    softwareReport_id = db.Column(db.Integer, db.ForeignKey('software.id'))

    def __repr__(self):
        return '<Report {}>'.format(self.name)
