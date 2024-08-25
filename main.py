from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/ASUS/Desktop/List of Top 10 movies/Movies.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

db = SQLAlchemy(app)
Bootstrap5(app)

MOVIE_DB_API_KEY = "386c1a3dd9acc3af765cb44446412420"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"


class addMovie(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

class MovieUpdateForm(FlaskForm):
    rating = IntegerField('Rating', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Update')

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

@app.route("/")
def home():
    all_movies = Movie.query.all()
    return render_template("index.html", movies=all_movies)

@app.route("/edit/<int:movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    form = MovieUpdateForm(obj=movie)
    
    if form.validate_on_submit():
        # Update movie details
        movie.rating = form.rating.data
        movie.review = form.review.data

        db.session.commit()
        flash('Movie updated successfully!', 'success')
        return redirect(url_for('home'))
    
    return render_template('edit.html', form=form, movie=movie)

@app.route("/delete/<int:id>")
def delete(id):
    movie_to_delete = Movie.query.get_or_404(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add_movie():
    form = addMovie()
    if form.validate_on_submit():
        movie_title = form.title.data  # Use form.title.data
        response = requests.get(MOVIE_DB_SEARCH_URL, params={
            "api_key": MOVIE_DB_API_KEY,
            "query": movie_title
        })
        data = response.json()["results"]
        
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)
@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={
            "api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()

        # Check if the movie already exists
        existing_movie = Movie.query.filter_by(title=data.get("title")).first()
        if existing_movie:
            flash('Movie already exists in the database.', 'info')
            return redirect(url_for("home"))

        # Add new movie if it doesn't exist
        new_movie = Movie(
            title=data["title"],
            year=int(data["release_date"].split("-")[0]),  # Convert year to integer
            img_url=f"{MOVIE_DB_IMAGE_URL}{data.get('poster_path', '')}",
            description=data.get("overview", ""),
            rating=None,  # Default to None
            ranking=None,  # Default to None
            review=""  # Default to empty string
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", movie_id=new_movie.id))  # Note: Changed to movie_id

    else:
        flash('No movie ID provided.', 'error')
        return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    app.run(debug=True)
