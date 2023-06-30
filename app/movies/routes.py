"""Summary this page contains the routes for the movies blueprint."""

from flask import render_template, request, jsonify
from app.movies import movies
from app import db
from app.star_trek_models import Movie

@movies.route('/')
def show_movies():
    """This page shows all the movies in the database."""
    
    movies = Movie.query.all()
    # must also send the movies back as json for the javascript to use
    return render_template('movies.html', movies=movies)


