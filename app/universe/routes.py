"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from flask import jsonify
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.animal_models import Animal
from app.schemas.animal_schema import AnimalSchema
from app.schemas.astronomical_objects_schema import AstronomicalObjectSchema
from app.schemas.character_schema import CharacterSchema
from app.models.star_trek_models import AstronomicalObject, Character
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

@universe.route('/animals/<name>')
def animal(name):
    """Returns a single animal from the database"""
    animal = AnimalSchema().dump(Animal.query.filter_by(name=name).first())
    
    # use the scraper to get the images and paragraphs from memory alpha
    scrapped_animal = MemoryAlphaScraper(replace_space(name))
    
    # NOTE: this hack is not working at the moment only returning the tribbles image
    # TODO need to implement a different method for scrapping images for animals
    images = scrapped_animal.get_images()
    image = images[0] if len(images) > 0 else tribbles
    info = scrapped_animal.get_paragraphs()
    
    return render_template('animal.html', animal=animal, title=name, info=info, image=image)



@universe.route('/astronomical-objects')
def astronomical_objects():
    """Returns all astronomical objects in the database"""
    astronomical_objects = AstronomicalObjectSchema(many=True).dump(AstronomicalObject.query.all())
    return render_template('astronomical_objects.html', astronomical_objects=astronomical_objects)

@universe.route('/astronomical-objects/<name>')
def astronomical_object(name):
    """Returns a single astronomical object from the database"""
    astronomical_object = AstronomicalObjectSchema().dump(AstronomicalObject.query.filter_by(name=name).first())
    return render_template('astronomical_object.html', astronomical_object=astronomical_object, title=name)

# NOTE: The characters route is not working at the moment
@universe.route('/characters')
def characters():
    """Returns all characters in the database"""
    characters = CharacterSchema(many=True).dump(Character.query.all())
    return render_template('characters.html', characters=characters)

@universe.route('/characters/<name>')
def character(name):
    """Returns a single character from the database"""
    character = CharacterSchema().dump(Character.query.filter_by(name=name).first())
    try:
        scrapped_character = MemoryAlphaScraper(replace_space(name))
        images = scrapped_character.get_images()
        image = images[0] if len(images) > 0 else tribbles
        info = scrapped_character.get_paragraphs()
    except Exception as e:
        print(e)
    return render_template('character.html', character=character, title=name, info=info, image=image)



