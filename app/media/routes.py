"""Summary this page contains the routes for the movies blueprint."""

from flask import render_template, request, jsonify
from app.media import media
from app import db
from app.models.star_trek_models import Series, Movie
from flask_restful import Resource, Api
from flask import jsonify

@media.route('/')
def media_index():
    """This page shows all media related to the Star Trek Universe."""
    return render_template('media.html')


# @movies.route('/')
# def show_movies():
#     """This page shows all the movies in the database."""
    
#     movies = Movie.query.all()
#     # must also send the movies back as json for the javascript to use
#     return render_template('movies.html', movies=movies)

# # make a request to the backend to get the movies
# @movies.route('/get_movies')
# def get_movies():
#     """This page shows all the movies in the database."""
        
#     movies = Movie.query.all()
#     # Serialize the movies using the MovieSchema
#     movie_schema = MovieSchema(many=True)
#     movies_json = movie_schema.dump(movies)
    
#     return jsonify(movies=movies_json)

# @movies.route('/test')
# def testing():
#     """Test request to for json"""
#     return jsonify({'test': 'test'})