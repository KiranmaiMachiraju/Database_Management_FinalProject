from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from flask_migrate import Migrate  # Import Migrate


# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Use a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Your database URI
db = SQLAlchemy(app)  # Initialize SQLAlchemy with app
migrate = Migrate(app, db)  # Initialize Flask-Migrate

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'auth'  # Redirect to login page if not logged in

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='books', lazy=True)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Google Books API Key
API_KEY = 'AIzaSyCyVgnY4TAUURkXoi9ba4JqhTSpucLFFcc'

# Home Page (Popular Books)
@app.route('/')
def index():
    url = f'https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=relevance&maxResults=10&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    books = []
    if 'items' in data:
        books = [{
            'title': item['volumeInfo'].get('title', 'No Title'),
            'author': item['volumeInfo'].get('authors', ['Unknown'])[0],
            'description': item['volumeInfo'].get('description', 'No description available'),
            'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
            'link': item['volumeInfo'].get('infoLink', '#')
        } for item in data['items']]

    return render_template('index.html', books=books)

# Auth (Login and Sign-up)
@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        # Handle Login
        if 'login' in request.form:
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()

            if user and check_password_hash(user.password, password):  # Assuming password is hashed
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))  # Redirect to dashboard after login
            else:
                flash('Invalid username or password.', 'danger')

        # Handle Sign Up
        elif 'signup' in request.form:
            username = request.form['username']
            password = request.form['password']
            user_exists = User.query.filter_by(username=username).first()

            if user_exists:
                flash('Username already taken. Please choose a different one.', 'danger')
            else:
                hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
                new_user = User(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()
                flash('Sign Up successful! You can now log in.', 'success')

    return render_template('auth.html')

# Dashboard Page (User's Books)
@app.route('/dashboard')
@login_required
def dashboard():
    print(current_user.username)  # Debug: check if the logged-in user is correct
    books = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', user=current_user)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.args.get('query')  # Get the search query from the URL
    books = []  # Default to an empty list in case of no results

    if query:
        # Search books using Google Books API based on query
        url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}'
        response = requests.get(url)
        data = response.json()

        if 'items' in data:
            books = [{
                'title': item['volumeInfo'].get('title', 'No Title'),
                'author': item['volumeInfo'].get('authors', ['Unknown'])[0],
                'description': item['volumeInfo'].get('description', 'No description available'),
                'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
                'link': item['volumeInfo'].get('infoLink', '#')
            } for item in data['items']]

    return render_template('search.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
