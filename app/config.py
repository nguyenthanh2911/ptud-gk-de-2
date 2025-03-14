import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/tasks.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # Limit upload size to 16 MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}