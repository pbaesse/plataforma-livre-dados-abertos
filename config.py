import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xdbq\x10\xf9\x11J6z\xee\xc4Y\x19oG[\x0c'
    RECAPTCHA_USE_SSL = False
    RECAPTCHA_PUBLIC_KEY='you-will-never-guess'
    RECAPTCHA_PRIVATE_KEY='you-will-never-guess'
    RECAPTCHA_OPTIONS= {'theme':'black'}
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    LANGUAGES = ['en', 'pt']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    POSTS_PER_PAGE = 20
    COMMENTS_PER_PAGE = 10
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
