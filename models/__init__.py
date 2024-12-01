from flask_sqlalchemy import SQLAlchemy

# Initialize the db object
db = SQLAlchemy()

# models/__init__.py
from .models import db, User, Book  # Import db, User, and Book from models.py