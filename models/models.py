# models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship  # Import relationship here
from flask_login import UserMixin

db = SQLAlchemy()

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Admin flag
    
    books = db.relationship('Book', back_populates='user')

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
