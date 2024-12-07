**Bookshelf Web Application **

The Bookshelf Web Application is a user-friendly platform that allows book enthusiasts to search, organize, and manage their personal book collections. It integrates with the Google Books API to offer book discovery and provides basic CRUD (Create, Read, Update, Delete) functionality for managing books in a database. 

Built using Flask for the backend, SQLAlchemy for database management, and HTML templates for the frontend, this application offers a dynamic yet simple approach to web development and database interaction. 

 

Project Details 

Features 

User Authentication: Users can log in and manage their profiles securely. 

Database Interaction: The application is connected to a relational database, allowing users to perform operations like adding, viewing, updating, and deleting records. 

Flask Routing: Various routes and templates are used to manage pages and views dynamically. 

Data Validation: Proper form validation is in place for CRUD operations, ensuring correct data handling. 

Bootstrap for Styling: Bootstrap is used to make the web pages look attractive and responsive across devices. 

Tech Stack 

Flask: Python web framework used for routing and handling HTTP requests. 

SQLAlchemy: Object Relational Mapping (ORM) tool to interact with databases using Python objects. 

SQLite or MySQL (Optional): The database management system used to store data. 

HTML, CSS, Bootstrap: For the frontend design of the application. 

Jinja2: Templating engine used in Flask to render dynamic content in HTML pages. 

Example Use Case 

Users: Manage their personal information or records stored in the database. 

Admin (Optional): Admin users can access the back-end interface to manage all user records. 

 

Getting Started with GitPod 

Step 1: Clone the Repository to GitPod 

Open your browser and navigate to the repository on GitHub: Database_Management_FinalProject. 

On the top-right corner of the page, click the green Code button and copy the repository URL. 

Open GitPod by going to https://gitpod.io. 

Paste the repository URL into the GitPod workspace setup page and hit Enter. 

Alternatively, you can open GitPod directly using this link: 

https://gitpod.io/#https://github.com/KiranmaiMachiraju/Database_Management_FinalProject 
  

This will automatically open a new GitPod workspace with the repository loaded. 

Step 2: Wait for GitPod to Set Up 

GitPod will automatically start a new environment, load the repository, and install the necessary tools (such as Python, Git, etc.) for you to begin working on the project. 

 

Setting Up the Python Environment 

Step 3: Install Python Libraries 

Once you're inside the GitPod workspace, open a Terminal window and run the following command to ensure that you have the necessary Python libraries installed. 

Install Flask and other required libraries: 

Ensure you are in the project directory by running: 

cd Database_Management_FinalProject 
  

Install Flask and other dependencies by running: 

pip install -r requirements.txt 
  

If requirements.txt doesn't exist or you want to install Flask manually, you can run: 

pip install flask 
pip install flask_sqlalchemy  # If you're using SQLAlchemy for database management. 
  

If your project requires additional libraries (e.g., for database interaction), make sure to install them as well. 

 

Running the Flask App 

Step 4: Run the Flask Application 

Once the libraries are installed, you can run your Flask application. 

Start the Flask server by running the following command in the terminal: 

python app.py 
  

The Flask app should now be running. GitPod typically opens a preview window for your app on a specific port (usually 5000). If it doesn't open automatically, you can manually open it: 

In the GitPod interface, look for the Preview option on the top-right side of the screen. 

Click on Preview and select Preview Port 5000 (or the correct port if different). 

Your Flask application should now be live, and you can interact with it through the browser. 

Troubleshooting 

Error: ModuleNotFoundError: No module named 'flask' 

If you receive an error saying that Flask is not installed, make sure you ran pip install flask to install the necessary libraries. 

Error: Port Not Opening 

If the Flask app does not open automatically in GitPod, make sure the terminal shows that the app is running on the correct port. You may have to manually open a preview of port 5000 as described earlier. 

 

Project Structure 

Here is an overview of the project's folder structure: 

Database_Management_FinalProject/ 
│ 
├── app.py                # Main Python file that runs the Flask app 
├── requirements.txt      # List of project dependencies (Flask, SQLAlchemy, etc.) 
├── templates/            # Contains all the HTML templates 
│   ├── index.html        # Home page template 
│   └── about.html        # About page template 
│ 
├── static/               # Contains static files (CSS, JavaScript, images, etc.) 
│   └── css/ 
│       └── app.css       # Custom CSS for styling 
│ 
└── README.md             # Project documentation (this file) 
  

app.py: The main entry point of the application, which contains the Flask routes and logic for handling HTTP requests. 

templates/: Directory that stores HTML templates, including index.html for the home page and about.html for the about page. 

static/: Directory containing static assets like CSS files, images, and JavaScript files. 

requirements.txt: A text file listing the Python dependencies, which can be installed using pip install -r requirements.txt. 

 

License 

This project is licensed under the MIT License - see the LICENSE file for details. 

 
