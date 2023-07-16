"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.animal_models import Animal
from app.schemas.animal_schema import AnimalSchema
from app.helpers import MemoryAlphaScraper

@universe.route('/')
def index():
    return render_template('universe.html')

@universe.route('/animals')
def animal_index():
    """Returns all animals in the database"""
    # I want to send that as a json object to the front end
    animals = Animal.query.all()
    canines = Animal.get_all_canine()
    felines = Animal.get_all_feline()
    earth_animals = Animal.get_all_earth_animals()
    earth_insects = Animal.get_all_earth_insects()
    avians = Animal.get_all_avian()
    print(canines) 
    return render_template('animals.html')
    

# When the route is requested 

@universe.route('/animals/results', methods=['GET','POST'])
def animal_results():
    """Returns a single animal from the database"""
    # gets the animals from the front end that needed images to be scraped via beautiful soup
    response = request.get_json()
    # extract the
    print(response["data"])
    
    return jsonify(response)
