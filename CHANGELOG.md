
### Changelog for app.py

#### 1. Overview
This document highlights the changes made to the app.py file in the project. The changes include new features, refactored code, and added functionality to enhance user experience and improve maintainability.

---

#### 2. Key Changes

1. **Integrated SQLAlchemy and Flask-Migrate:**
   - Added flask_sqlalchemy for database management and flask_migrate for database migrations.
   - Initialized SQLAlchemy and Flask-Migrate:
     ```python
     from flask_sqlalchemy import SQLAlchemy
     from flask_migrate import Migrate
     db = SQLAlchemy(app)
     migrate = Migrate(app, db)
     ```

2. **User Authentication with Flask-Login:**
   - Integrated flask_login for handling user login/logout and session management.
   - Created a User model for managing user accounts:
     ```python
     class User(UserMixin, db.Model):
         id = db.Column(db.Integer, primary_key=True)
         username = db.Column(db.String(150), unique=True, nullable=False)
         password = db.Column(db.String(150), nullable=False)
     ```
   - Added login_manager for session management and user loading:
     ```python
     login_manager = LoginManager(app)
     login_manager.login_view = 'auth'
     ```

3. **Google Books API Integration:**
   - Implemented functionality to fetch book data from the Google Books API.
   - Example: Fetching popular fiction books on the home page:
     ```python
     url = f'https://www.googleapis.com/books/v1/volumes?q=subject:fiction&orderBy=relevance&maxResults=10&key={API_KEY}'
     response = requests.get(url)
     ```

4. **Dashboard Implementation:**
   - Added a user-specific dashboard to display books associated with the logged-in user:
     ```python
     @app.route('/dashboard')
     @login_required
     def dashboard():
         books = Book.query.filter_by(user_id=current_user.id).all()
         return render_template('dashboard.html', user=current_user)
     ```

5. **Search Functionality:**
   - Integrated a search page that allows users to search for books using the Google Books API:
     ```python
     @app.route('/search', methods=['GET', 'POST'])
     def search():
         query = request.args.get('query')
         # Search logic here
     ```

6. **Enhanced Error Handling and Flash Messages:**
   - Used flask.flash to provide feedback for login, signup, and other actions:
     ```python
     flash('Login successful!', 'success')
     flash('Invalid username or password.', 'danger')
     ```

7. **Refactored Routing and Template Rendering:**
   - Organized routes for login, signup, logout, and other functionalities.
   - Added render_template calls for better separation of logic and UI.

8. **New Models:**
   - Added a Book model to manage user-specific books in the database:
     ```python
     class Book(db.Model):
         id = db.Column(db.Integer, primary_key=True)
         title = db.Column(db.String(150), nullable=False)
         ...
     ```

---

#### 3. How to Use the Updated Version
1. **Install Required Dependencies:**
   ```bash
   pip install flask flask_sqlalchemy flask_login flask_migrate requests
   ```

2. **Set Up the Database:**
   - Initialize and migrate the database:
     ```bash
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```

3. **Run the Application:**
   - Start the Flask app:
     ```bash
     flask run
     ```

4. **Test Features:**
   - Test login/signup functionality.
   - Verify book search and dashboard display.

---

#### 4. Future Enhancements
- Add book CRUD operations (Create, Read, Update, Delete).
- Implement role-based access control for different user types.
- Enhance search with advanced filters (e.g., genre, rating).

---
