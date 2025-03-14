import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'tasks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    UPLOAD_FOLDER = os.path.join(basedir, 'app', 'static', 'avatars')

class TestingConfig:
    TESTING = True
    SECRET_KEY = 'test-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False

class DevelopmentConfig:
    DEBUG = True
    SECRET_KEY = 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'tasks_dev.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': Config
}