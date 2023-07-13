"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from app.universe import universe
from flask import render_template
from app.models.star_trek_models import Animal

@universe.route('/')
def index():
    return render_template('universe.html')

@universe.route('/animals')
def show_animals():
    animals = Animal.query.all()
    return render_template('animals.html', animals=animals)