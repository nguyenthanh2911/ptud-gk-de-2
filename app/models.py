from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    avatar = db.Column(db.String(120), default='default.png')
    is_admin = db.Column(db.Boolean, default=False)
    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @property
    def overdue_count(self):
        return Task.query.filter_by(user_id=self.id, finished=None).filter(
            Task.deadline < datetime.utcnow()).count()
    
    def __repr__(self):
        return f'<User {self.username}>'

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, in_progress, completed
    created = db.Column(db.DateTime, default=datetime.utcnow)
    deadline = db.Column(db.DateTime)
    finished = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def is_overdue(self):
        return not self.finished and self.deadline and self.deadline < datetime.utcnow()
    
    def __repr__(self):
        return f'<Task {self.title}>'