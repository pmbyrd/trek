"""This file handles routing for the api blueprint.
The api will make calls to the database and return json data.
It does this by using the schemas to serialize the data.
Making it a centralized location for the api to get data from the database.
"""

from app.api import api
from flask import jsonify
from app.models.animal_models import Animal
from app.schemas.animal_schema import AnimalSchema

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
