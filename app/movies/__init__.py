"""Summary = This page initializes the movies blueprint."""

from flask import Blueprint

movies = Blueprint(
    'movies', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/movies'
    )

from app.movies import routes