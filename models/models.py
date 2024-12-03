# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Admin flag

    books = db.relationship('Book', back_populates='user')

    def __repr__(self):
        return f'<User {self.username}>'

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    description = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    thumbnail = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    order_index = db.Column(db.Integer)  # New column to store the order index

    user = db.relationship('User', back_populates='books')

    def __repr__(self):
        return f'<Book {self.title}>'

# Activity Model to log actions for both logged-in and logged-out users
class RecentActivity(db.Model):
    __tablename__ = 'recent_activity'

    id = db.Column(db.Integer, primary_key=True)
    activity_type = db.Column(db.String(100), nullable=False)  # e.g., 'searched_book', 'added_book', 'removed_book'
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    description = db.Column(db.String(255), nullable=True)  # Optional: additional description of activity

    # user_id is nullable, as guests (logged-out users) won't have a user_id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  
    user = relationship('User', backref='recent_activities', lazy=True)

    def __repr__(self):
        return f'<RecentActivity {self.activity_type} by {self.user.username if self.user else "Guest"}>'