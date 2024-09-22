from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    progress = db.Column(db.Integer, default=0)
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

    def __repr__(self):
        return f'<Lesson {self.subject} - {self.topic}>'
    
    # Add the Progress model if it doesn't exist
class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other fields as needed
    # For example:
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # lesson_id = db.Column(db.Integer, nullable=False)
    # completed = db.Column(db.Boolean, default=False)
    # ... other fields ...

    def __repr__(self):
        return f'<Progress {self.id}>'
    

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer)
    category = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    user = db.relationship('User', back_populates='feedback')

    def __repr__(self):
        return f'<Feedback {self.id} by User {self.user_id}>'
