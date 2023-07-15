"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.star_trek_models import Animal
from app.schemas.animal_schema import AnimalSchema
from app.helpers import ma_article

@universe.route('/')
def index():
    return render_template('universe.html')

@universe.route('/animals')
def show_animals():
    animals = Animal.query.all()
    return render_template('animals.html', animals=animals)


@universe.route('/animals/results', methods=['GET','POST'])
def animal_results():
    """Returns a single animal from the database"""
    # gets the animals from the front end that needed images to be scraped via beautiful soup
    response = request.get_json()
    # extract the
    print(response["data"])
    
    return jsonify(response)
