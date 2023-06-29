"""Summary: This file contains the routes for the quadrants blueprint.
"""

# Make sure to import the blueprint
from app.quadrants import quadrants
from flask import render_template
from app.star_trek_models import Animal

@quadrants.route('/')
def index():
    return render_template('quadrants.html')

@quadrants.route('/animals')
def show_animals():
    animals = Animal.query.all()
    return render_template('animals.html', animals=animals)