"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from flask import jsonify
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.animal_models import Animal
from app.schemas.animal_schema import AnimalSchema
from app.schemas.astronomical_objects_schema import AstronomicalObjectSchema
from app.models.star_trek_models import AstronomicalObject
from app.helpers import MemoryAlphaScraper, replace_space
from app.images.defaults import tribbles
from random import choices

import json


@universe.route('/')
def index():
    return render_template('universe.html')


@universe.route('/animals')
def animals():
    """Returns all animals in the database"""
    animals = AnimalSchema(many=True).dump(Animal.query.all())

    return render_template('animals.html', animals=animals)


@universe.route('/animals/samples')
def animal_index():
    """Returns all animals in the database and sends them as a JSON object to the front end"""
    animals = AnimalSchema(many=True).dump(Animal.query.all())
    categories = {
        'canines': Animal.get_all_canine(),
        'felines': Animal.get_all_feline(),
        'earth_animals': Animal.get_all_earth_animals(),
        'earth_insects': Animal.get_all_earth_insects(),
        'avians': Animal.get_all_avian()
    }

    for category in categories:
        categories[category] = [animal.name for animal in categories[category]]
        print(categories[category][:5])
        
    # use choices to a random animal from each animal category
    random_animals = {
        "canine": [choices(categories["canines"], k=3 )],
        "feline": [choices(categories["felines"], k=3 )],
        "earth_animal": [choices(categories["earth_animals"], k=3 )],
        "earth_insect": [choices(categories["earth_insects"], k=3 )],
        "avian": [choices(categories["avians"], k=3)]
    }
    
    # the random_animals need to be serialized before they can be sent to the front end
    json_random_animals = json.dumps(random_animals, indent=4, sort_keys=True, default=str)
    
    print("json random animals")
    print(json_random_animals)
    print("random animals")
    print(random_animals)
    
    return jsonify(animals, json_random_animals)


@universe.route('/animals/results', methods=['GET', 'POST'])
def animal_results():
    """Returns a single animal from the database"""
    # gets the animals from the front end that needed images to be scraped via beautiful soup
    response = request.get_json()
    # extract the
    print(response["data"])

    return jsonify(response)

@universe.route('/astronomical-objects')
def astronomical_objects():
    """Returns all astronomical objects in the database"""
    return render_template('astronomical_objects.html')

@universe.route('/astronomical-objects/samples')
def astronomical_objects_index():
    """Returns all astronomical objects in the database and sends them as a JSON object to the front end"""
    astronomical_objects = AstronomicalObjectSchema(many=True).dump(AstronomicalObject.query.all())
    return jsonify(astronomical_objects)