# app/models.py
from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    progress = db.relationship('Progress', backref='user', lazy='dynamic')
    feedbacks = db.relationship('Feedback', backref='user', lazy='dynamic')
    current_subject = db.Column(db.String(64), default='Python')
    current_topic = db.Column(db.String(128), default='Introduction')
    last_activity = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(64), nullable=False)
    topic = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    progresses = db.relationship('Progress', backref='lesson', lazy='dynamic')

    def __repr__(self):
        return f'<Lesson {self.subject} - {self.topic}>'

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'), nullable=False)
    attempts = db.Column(db.Integer, default=0)
    completed = db.Column(db.Boolean, default=False)
    last_attempt = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Progress {self.id} - User {self.user_id} - Lesson {self.lesson_id}>'

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(64))
    topic = db.Column(db.String(128))
    code = db.Column(db.Text)
    feedback_text = db.Column(db.Text)
    rating = db.Column(db.Integer)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Feedback {self.id} by User {self.user_id}>'
