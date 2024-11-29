from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from flask_migrate import Migrate

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
    order_index = db.Column(db.Integer, default=0)  # For storing book order

    user = db.relationship('User', backref='books', lazy=True)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Google Books API Key
API_KEY = 'AIzaSyCyVgnY4TAUURkXoi9ba4JqhTSpucLFFcc'  # Your API key

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
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    # Get sorting options from query parameters
    sort_by = request.args.get('sort_by', 'title')  # Default to sorting by title
    order = request.args.get('order', 'asc')  # Default to ascending order

    # Fetch books for the current user
    if sort_by == 'title':
        books = Book.query.filter_by(user_id=current_user.id).order_by(
            Book.title.asc() if order == 'asc' else Book.title.desc()
        ).all()
    elif sort_by == 'author':
        books = Book.query.filter_by(user_id=current_user.id).order_by(
            Book.author.asc() if order == 'asc' else Book.author.desc()
        ).all()
    elif sort_by == 'rating':
        books = Book.query.filter_by(user_id=current_user.id).order_by(
            Book.rating.desc() if order == 'desc' else Book.rating.asc()
        ).all()
    else:
        books = Book.query.filter_by(user_id=current_user.id).all()  # Default case

    # Handle search functionality if submitted
    if request.method == 'POST':
        query = request.form.get('query')  # Search query
        if query:
            url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}'
            response = requests.get(url)
            data = response.json()

            search_results = []
            if 'items' in data:
                search_results = [{
                    'title': item['volumeInfo'].get('title', 'No Title'),
                    'author': item['volumeInfo'].get('authors', ['Unknown'])[0],
                    'description': item['volumeInfo'].get('description', 'No description available'),
                    'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
                } for item in data['items']]

            return render_template('dashboard.html', user=current_user, books=books, search_results=search_results)

    return render_template('dashboard.html', user=current_user, books=books)

# Add Book to Shelf
@app.route('/add_book', methods=['POST'])
@login_required
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    description = request.form.get('description')
    genre = request.form.get('genre')
    rating = request.form.get('rating')

    # Add the book to the database
    new_book = Book(title=title, author=author, description=description, genre=genre, rating=rating, user_id=current_user.id)
    db.session.add(new_book)
    db.session.commit()
    flash(f'Book "{title}" added to your shelf!', 'success')
    return redirect(url_for('dashboard'))

# Update Book Order (via drag-and-drop)
@app.route('/update_order', methods=['POST'])
@login_required
def update_order():
    # Retrieve the updated order of books from the request
    book_ids = request.json.get('book_ids')
    for index, book_id in enumerate(book_ids):
        book = Book.query.get(book_id)
        if book:
            book.order_index = index  # Save the order to the database
            db.session.commit()
    return {'status': 'success'}, 200

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Search Books
@app.route('/search', methods=['GET', 'POST'])
def search():
    search_results = []
    if request.method == 'POST':
        query = request.form.get('query')  # Get the search query
        if query:
            url = f'https://www.googleapis.com/books/v1/volumes?q={query}&key={API_KEY}'
            response = requests.get(url)
            data = response.json()

            # Check if there are any books returned
            if 'items' in data:
                search_results = [{
                    'title': item['volumeInfo'].get('title', 'No Title'),
                    'author': item['volumeInfo'].get('authors', ['Unknown'])[0],
                    'description': item['volumeInfo'].get('description', 'No description available'),
                    'thumbnail': item['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''),
                    'link': item['volumeInfo'].get('infoLink', '#')
                } for item in data['items']]

    return render_template('search.html', books=search_results)

if __name__ == '__main__':
    app.run(debug=True)