Flask Movie Management System

A Flask application for managing a list of top movies. This application allows you to add, edit, and delete movies. It integrates with The Movie Database (TMDb) API to fetch movie details and allows users to rate and review movies.
Features

    Add Movies: Search for movies using the TMDb API and add them to your database.
    Edit Movies: Update movie ratings and reviews.
    Delete Movies: Remove movies from your database.
    View Movies: Display a list of all movies in the database.

Installation

    Clone the repository

    bash

git clone https://github.com/yourusername/your-repository.git
cd your-repository

Create a virtual environment

bash

python -m venv venv

Activate the virtual environment

    On Windows:

    bash

venv\Scripts\activate

On macOS/Linux:

bash

    source venv/bin/activate

Install the required packages

bash

pip install -r requirements.txt

Create the database

Run the application once to create the database schema:

bash

    python app.py

Configuration

    Database URI: Update the SQLALCHEMY_DATABASE_URI in app.py to point to your database file.

    python

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///path/to/your/database.db"

TMDb API Key: Replace MOVIE_DB_API_KEY with your own TMDb API key.

python

    MOVIE_DB_API_KEY = "your_api_key"

Usage

    Run the Application

    bash

    python app.py

    The application will be available at http://127.0.0.1:5000.

    Navigate the Application
        Home Page: View all movies.
        Add Movie: Search for and add new movies.
        Edit Movie: Update movie details (rating and review).
        Delete Movie: Remove movies from the list.

Code Overview

    app.py: Main application file containing routes and database models.
    templates/: Contains HTML templates used by Flask.
    static/: Contains static files such as CSS and JavaScript.

Example Routes

    Home Page: GET /
    Add Movie: GET /add, POST /add
    Find Movie: GET /find
    Edit Movie: GET /edit/<movie_id>, POST /edit/<movie_id>
    Delete Movie: GET /delete/<id>

License

This project is licensed under the MIT License. See the LICENSE file for details.
