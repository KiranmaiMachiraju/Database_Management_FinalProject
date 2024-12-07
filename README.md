# Bookshelf Web Application

The **Bookshelf Web Application** is a user-friendly platform that allows book enthusiasts to search, organize, and manage their personal book collections. It integrates with the **Google Books API** to offer book discovery and provides basic **CRUD (Create, Read, Update, Delete)** functionality for managing books in a database.

Built using **Flask** for the backend, **SQLAlchemy** for database management, and **HTML templates** for the frontend, this application offers a dynamic yet simple approach to web development and database interaction.

## Project Details

### Features
- **User Authentication**: Users can log in and manage their profiles securely.
- **Database Interaction**: The application is connected to a relational database, allowing users to perform operations like adding, viewing, updating, and deleting records.
- **Flask Routing**: Various routes and templates are used to manage pages and views dynamically.
- **Data Validation**: Proper form validation is in place for CRUD operations, ensuring correct data handling.
- **Bootstrap for Styling**: Bootstrap is used to make the web pages look attractive and responsive across devices.

### Tech Stack
- **Flask**: Python web framework used for routing and handling HTTP requests.
- **SQLAlchemy**: Object Relational Mapping (ORM) tool to interact with databases using Python objects.
- **SQLite** (default) or **MySQL** (optional): Database management systems used to store data.
- **HTML, CSS, Bootstrap**: For the frontend design of the application.
- **Jinja2**: Templating engine used in Flask to render dynamic content in HTML pages.

### Example Use Case
- **Users**: Manage their personal information or records stored in the database.
- **Admin (Optional)**: Admin users can access the back-end interface to manage all user records.

## Getting Started with GitPod

### Step 1: Clone the Repository to GitPod
1. Open your browser and navigate to the repository on GitHub: [Database_Management_FinalProject](https://github.com/KiranmaiMachiraju/Database_Management_FinalProject).
2. On the top-right corner of the page, click the green **Code** button and copy the repository URL.
3. Open GitPod by going to [https://gitpod.io](https://gitpod.io).
4. Paste the repository URL into the GitPod workspace setup page and hit Enter.
   - Alternatively, open GitPod directly with this link:  
     [https://gitpod.io/#https://github.com/KiranmaiMachiraju/Database_Management_FinalProject](https://gitpod.io/#https://github.com/KiranmaiMachiraju/Database_Management_FinalProject).

This will automatically open a new GitPod workspace with the repository loaded.

### Step 2: Wait for GitPod to Set Up

GitPod will automatically start a new environment, load the repository, and install the necessary tools (such as Python, Git, etc.) for you to begin working on the project.

## Setting Up the Python Environment

### Step 3: Install Python Libraries

Once you're inside the GitPod workspace, open a Terminal window and run the following command to ensure that you have the necessary Python libraries installed.

Install Flask and other required libraries:

1. Ensure you are in the project directory by running:

    ```bash
    cd Database_Management_FinalProject
    ```

2. Install Flask and other dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

   If `requirements.txt` doesn't exist or you want to install Flask manually, you can run:

    ```bash
    pip install flask
    pip install flask_sqlalchemy  # If you're using SQLAlchemy for database management.
    ```

3. If your project requires additional libraries (e.g., for database interaction), make sure to install them as well.

### Running the Flask App

### Step 4: Run the Flask Application

Once the libraries are installed, you can run your Flask application.

Start the Flask server by running the following command in the terminal:

```bash
python app.py
```

The Flask app should now be running. GitPod typically opens a preview window for your app on a specific port (usually 5000). If it doesn't open automatically, you can manually open it:

1. In the GitPod interface, look for the **Preview** option on the top-right side of the screen.
2. Click on **Preview** and select **Preview Port 5000** (or the correct port if different).

Your Flask application should now be live, and you can interact with it through the browser.

## Troubleshooting

### Error: ModuleNotFoundError: No module named 'flask'

If you receive an error saying that Flask is not installed, make sure you ran:

```bash
pip install flask
```

### Error: Port Not Opening

If the Flask app does not open automatically in GitPod, make sure the terminal shows that the app is running on the correct port. You may have to manually open a preview of port 5000 as described earlier.

## Project Structure

Here is an overview of the project's folder structure:

```
Database_Management_FinalProject/
│
├── app.py                # Main Python file that runs the Flask app
├── config.py             # Configuration file for Flask settings (if exists)
├── requirements.txt      # List of project dependencies (Flask, SQLAlchemy, etc.)
├── .gitignore            # Git ignore file to exclude unnecessary files
├── README.md             # Project documentation (this file)
│
├── static/               # Contains static files (CSS, JavaScript, images, etc.)
│   ├── css/              # Custom CSS files
│   │   ├── app.css       # Custom CSS for styling
│   │   └── bootstrap.min.css  # Bootstrap CSS (if included)
│   ├── js/               # JavaScript files
│   │   ├── app.js        # Custom JS for functionality
│   │   └── jquery.min.js # jQuery (if included)
│   └── images/           # Folder for images
│       └── logo.png      # Logo image (if included)
│
├── templates/            # Contains all HTML templates
│   ├── admin_login.html  # Admin login page
│   ├── admin_dashboard.html # Admin dashboard page
│   ├── auth.html         # Login and sign-up page
│   ├── dashboard.html    # User's dashboard page
│   ├── home.html         # Home page template
│   ├── index.html        # Index page (displays Google Books API data)
│   └── search.html       # Search results page for books
│
├── models/               # Database models directory
│   ├── __init__.py       # Initializes the models package
│   ├── user.py           # User model for database interactions
│   ├── book.py           # Book model for book-related data
│   └── recent_activity.py # Recent activity model for tracking user actions
│
├── migrations/           # Flask-Migrate migrations folder
│   └── versions/         # Migration version scripts
│       └── abc123_def456.py  # Example migration file
|
```

- app.py: The core file where Flask routes are defined, user login is managed, and the Google Books API is accessed.
- config.py: This is typically where configurations for the app are stored, such as secret keys, database URIs, and third-party API keys (like the Google Books API). This might not be in your existing project but is a good practice to include.
- requirements.txt: List of dependencies like Flask, Flask-SQLAlchemy, Flask-Login, etc.
- .gitignore: File to specify which files/folders to ignore when pushing to GitHub (like virtual environments, database files, etc.).
- README.md: Project documentation with setup instructions and feature explanations.
- static/: Stores CSS, JS, and image files.
- templates/: Stores HTML files for rendering views. These files interact with your backend (Flask routes) and provide dynamic content like user dashboards and search results.
- models/: Contains Python classes defining your database schema using SQLAlchemy (e.g., User, Book, RecentActivity).
- migrations/: Used by Flask-Migrate to store migration scripts for changing the database schema over time.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
