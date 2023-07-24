"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from flask import jsonify
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.animal_models import Animal
from app.models.star_trek_models import AstronomicalObject, Character, Occupation, Organization, SpacecraftClass, Spacecraft, Species, Technology, Weapon
from app.schemas.animal_schema import AnimalSchema
from app.schemas.astronomical_objects_schema import AstronomicalObjectSchema
from app.schemas.occupation_schema import OccupationSchema
from app.schemas.character_schema import CharacterSchema
from app.schemas.organization_schema import OrganizationSchema
from app.schemas.spacecraft_class_schema import SpacecraftClassSchema
from app.schemas.spacecraft_schema import SpacecraftSchema
from app.schemas.species_schema import SpeciesSchema
from app.schemas.technology_schema import TechnologySchema
from app.schemas.weapon_schema import WeaponSchema
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

#NOTE: The occupations route is not working at the moment
@universe.route('/occupations')
def occupations():
    """Returns all occupations in the database"""
    occupations = OccupationSchema(many=True).dump(Occupation.query.all())
    return render_template('occupations.html', occupations=occupations, title='Occupations')
#NOTE: the organizations route is not working at the moment
@universe.route('/organizations')
def organizations():
    """Returns all organizations in the database"""
    organizations = OrganizationSchema(many=True).dump(Organization.query.all())
    return render_template('organizations.html', organizations=organizations, title='Organizations')

@universe.route('/organizations/<name>')
def organization(name):
    """Returns a single organization from the database"""
    organization = OrganizationSchema().dump(Organization.query.filter_by(name=name).first())
    return render_template('organization.html', organization=organization, title=name)

#NOTE: The spacecrafts classes is not pulling up the correct data, it seems to be pulling for locations instead
# 
@universe.route('/spacecrafts-classes')
def spacescraft_classes():
    """Returns all spacecraft classes in the database"""
    spacecrafts_classes = AstronomicalObjectSchema(many=True).dump(AstronomicalObject.query.all())
    return render_template('spacecrafts_classes.html', spacecrafts_classes=spacecrafts_classes)

#NOTE may not be worth implementing until I can fix the data issue
# @universe.route('/spacecrafts-classes/<name>')
# def spacecraft_class(name):
#     """Returns a single spacecraft class from the database"""
#     spacecraft_class = SpacecraftClassSchema().dump(SpacecraftClass.query.filter_by(name=name).first())
#     return render_template('spacecraft_class.html', spacecraft_class=spacecraft_class, title=name)

#NOTE data is returning all blanks at the moment
@universe.route('/spacecrafts')
def spacecrafts():
    """Returns all spacecrafts in the database"""
    spacecrafts = SpacecraftSchema(many=True).dump(Spacecraft.query.all())
    return render_template('spacecrafts.html', spacecrafts=spacecrafts)

@universe.route('/species_all')
def species():
    """Returns all species in the database"""
    # species_all = SpeciesSchema(many=True).dump(Species.query.all())
    # return render_template('species_all.html', species_all=species_all)
    species_all = Species.query.all()
    #FIXME - Neither one of these implementations are working
    print(Species.query.first())
    return render_template('species_all.html', species_all=species_all)
    
@universe.route('/technologies')
def technologies():
    """Returns all technologies in the database"""
    technologies = TechnologySchema(many=True).dump(Technology.query.all())
    return render_template('technologies.html', technologies=technologies)

#NOTE weapons is also blank
@universe.route('/weapons')
def weapons():
    """Returns all weapons in the database"""
    weapons = WeaponSchema(many=True).dump(Weapon.query.all())
    weapons_ = Weapon.query.all()
    print(Weapon.query.first())
    return render_template('weapons.html', weapons=weapons, weapons_=weapons_)