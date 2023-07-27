"""This file handles routing for the api blueprint.
The api will make calls to the database and return json data.
It does this by using the schemas to serialize the data.
Making it a centralized location for the api to get data from the database.
"""

from app.api import api
from flask import jsonify
from app.models.animal_models import Animal
from app.models.star_trek_models import Character, AstronomicalObject, Movie
from app.schemas.animal_schema import AnimalSchema
from app.schemas.character_schema import CharacterSchema
from app.schemas.astronomical_objects_schema import AstronomicalObjectSchema
from app.schemas.movie_schema import MovieSchema

@api.route('/api/test')
def testing():
    """Test request to for json"""
    return jsonify({'test': 'test'})

@api.route('/api/animals')
def animals():
    """Returns all animals in the database"""
    animals = AnimalSchema(many=True).dump(Animal.query.all())
    return jsonify(animals)

@api.route('/api/animal/<int:id>')
def animal(id):
    """Returns a single animal from the database"""
    animal = AnimalSchema().dump(Animal.query.get(id))
    return jsonify(animal)

@api.route('/api/astronomical-objects')
def astronomical_objects():
    """Returns all astronomical objects in the database"""
    astronomical_objects = AstronomicalObjectSchema(many=True).dump(AstronomicalObject.query.all())
    return jsonify(astronomical_objects)

@api.route('/api/characters')
def characters():
    """Returns all characters in the database"""
    characters = CharacterSchema(many=True).dump(Character.query.all())
    print(characters[:10])
    return jsonify(characters)

@api.route('/api/movies')
def json_movies():
    """Returns all movies in the database"""
    movies = MovieSchema(many=True).dump(Movie.query.all())
    return jsonify(movies)