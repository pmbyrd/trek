"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from flask import jsonify
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.animal_models import Animal
from app.models.star_trek_models import Material, Title, AstronomicalObject, Character,Food, Element, Location, Conflict, Occupation, Organization, SpacecraftClass, Spacecraft, Species, Technology, Weapon
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
from app.static.img.defaults import tribbles
from random import choices

import json


@universe.route('/')
def index():
    return render_template('universe.html')

@universe.route('/animals')
def animals():
    """Returns all animals in the database"""
    page = request.args.get('page', 1, type=int)
    animals = Animal.query.order_by(Animal.name.asc()).all()
    paginated_animals = Animal.query.order_by(Animal.name.asc()).paginate(page=page, per_page=25)
    
    return render_template('animals.html', animals=animals, title='Animals', page=page, paginated_animals=paginated_animals)

@universe.route('/animals/<name>')
def animal(name):
    """Returns a single animal from the database"""
    animal = AnimalSchema().dump(Animal.query.filter_by(name=name).first())
    
    
    try:     
        scrapped_animal = MemoryAlphaScraper(replace_space(name))
        summary = scrapped_animal.get_summary()
        get_info = scrapped_animal.get_formatted_info()
        if summary:
            print("summary found")
        elif not summary:
            print("summary not found")
        else:
            print("summary is not iterable")
        if get_info:
            print("info found")
        else:
            print("info not found")
        # import pdb; pdb.set_trace()
        return render_template('animal.html', animal=animal, title=name, summary=summary, get_info=get_info)
    except TypeError as Nonetype:
        if Nonetype:
            print(Nonetype)
            paired_elements = None
            return render_template('animal.html', animal=animal, title=name)


@universe.route('/astronomical-objects')
def astronomical_objects():
    """Returns all astronomical objects in the database"""
    page = request.args.get('page', 1, type=int)
    astronomical_objects = AstronomicalObject.query.order_by(AstronomicalObject.name.asc()).all()
    paginated_astronomical_objects = AstronomicalObject.query.order_by(AstronomicalObject.name.asc()).paginate(page=page, per_page=25)
    
    return render_template('astronomical_objects.html', astronomical_objects=astronomical_objects, title='Astronomical Objects', page=page, paginated_astronomical_objects=paginated_astronomical_objects)

@universe.route('/astronomical-objects/<name>')
def astronomical_object(name):
    """Returns a single astronomical object from the database"""
    astronomical_object = AstronomicalObjectSchema().dump(AstronomicalObject.query.filter_by(name=name).first())
    try:
        scarpped_astronomical_object = MemoryAlphaScraper(replace_space(name))
        summary = scarpped_astronomical_object.get_summary()
        if summary:
            return render_template('astronomical_object.html', astronomical_object=astronomical_object, summary=summary, title=name)
        else:
            print("summary not found")
            raise TypeError
    except Exception as e:
        return "Error: " + str(e)
    
    
@universe.route('/characters')
def characters():
    """Returns all characters in the database"""
    # characters = CharacterSchema(many=True).dump(Character.query.all())4
    characters = Character.query.all()
    return render_template('characters.html', characters=characters, title='Characters')

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

@universe.route('/conflicts')
def conflicts():
    """Returns all conflicts in the database"""
    conflicts = Conflict.query.all()
    return render_template('conflicts.html', conflicts=conflicts, title='Conflicts')

@universe.route('/conflicts/<name>')
def conflict(name):
    """Returns a single conflict from the database"""
    conflict = Conflict.query.filter_by(name=name).first()
    try:
        scrapped_conflict = MemoryAlphaScraper(replace_space(name))
        images = scrapped_conflict.get_images()
        image = images[0] if len(images) > 0 else tribbles
        info = scrapped_conflict.get_paragraphs()
    except Exception as e:
        print (e)
    return render_template('conflict.html', conflict=conflict, title=name, info=info, image=image)

@universe.route('/elements')
def elements():
    """Returns all elements in the database"""
    elements = Element.query.all()
    return render_template('elements.html', elements=elements, title='Elements')

@universe.route('/elements/<name>')
def element(name):
    """Returns a single element from the database"""
    element = Element.query.filter_by(name=name).first()
    try:
        scrapped_element = MemoryAlphaScraper(replace_space(name))
        images = scrapped_element.get_images()
        image = images[0] if len(images) > 0 else tribbles
        info = scrapped_element.get_paragraphs()
    except Exception as e:
        print (e)
    return render_template('element.html', element=element, title=name, info=info, image=image)

@universe.route('/foods')
def foods():
    """Returns all foods in the database"""
    foods = Food.query.all()
    return render_template('foods.html', foods=foods, title='Foods')

@universe.route('/foods/<name>')
def food(name):
    """Returns a single food from the database"""
    food = Food.query.filter_by(name=name).first()
    try:
        scrapped_food = MemoryAlphaScraper(replace_space(name))
        images = scrapped_food.get_images()
        image = images[0] if len(images) > 0 else tribbles
        info = scrapped_food.get_paragraphs()
    except Exception as e:
        print (e)
    return render_template('food.html', food=food, title=name, info=info, image=image)

@universe.route('/locations')
def locations():
    """Returns all locations in the database"""
    locations = Location.query.all()
    return render_template('locations.html', locations=locations, title='Locations')

@universe.route('/locations/<name>')
def location(name):
    """Returns a single location from the database"""
    location = Location.query.filter_by(name=name).first()
    try:
        scrapped_location = MemoryAlphaScraper(replace_space(name))
        images = scrapped_location.get_images()
        image = images[0] if len(images) > 0 else tribbles
        info = scrapped_location.get_paragraphs()
    except Exception as e:
        print (e)
    return render_template('location.html', location=location, title=name, info=info, image=image)

@universe.route('/materials')
def materials():
    """Returns all materials in the database"""
    materials = Material.query.all()
    return render_template('materials.html', materials=materials, title='Materials')

@universe.route('/materials/<name>')
def material(name):
    """Returns a single material from the database"""
    material = Material.query.filter_by(name=name).first()
    return render_template('material.html', material=material, title=name)

#NOTE: The occupations route is not working at the moment
@universe.route('/occupations')
def occupations():
    """Returns all occupations in the database"""
    occupations = Occupation.query.all()
    return render_template('occupations.html', occupations=occupations, title='Occupations')

@universe.route('/occupations/<name>')
def occupation(name):
    """Returns a single occupation from the database"""
    occupation = Occupation.query.filter_by(name=name).first()
    return render_template('occupation.html', occupation=occupation, title=name)

@universe.route('/organizations')
def organizations():
    """Returns all organizations in the database"""
    organizations = Organization.query.all()
    return render_template('organizations.html', organizations=organizations, title='Organizations')

@universe.route('/organizations/<name>')
def organization(name):
    """Returns a single organization from the database"""
    organization = OrganizationSchema().dump(Organization.query.filter_by(name=name).first())
    return render_template('organization.html', organization=organization, title=name)

@universe.route('/spacecrafts-classes')
def spacecraft_classes():
    """Returns all spacecraft classes in the database"""
    spacecrafts_classes = AstronomicalObjectSchema(many=True).dump(AstronomicalObject.query.all())
    return render_template('spacecrafts_classes.html', spacecrafts_classes=spacecrafts_classes, title='Spacecrafts Classes')

@universe.route('/spacecrafts-classes/<name>')
def spacecraft_class(name):
    """Returns a single spacecraft class from the database"""
    spacecraft_class = SpacecraftClassSchema().dump(SpacecraftClass.query.filter_by(name=name).first())
    return render_template('spacecraft_class.html', spacecraft_class=spacecraft_class, title=name)


@universe.route('/spacecrafts')
def spacecrafts():
    """Returns all spacecrafts in the database"""
    spacecrafts = Spacecraft.query.all()
    return render_template('spacecrafts.html', spacecrafts=spacecrafts)

@universe.route('/spacecrafts/<name>')
def spacecraft(name):
    """Returns a single spacecraft from the database"""
    spacecraft = Spacecraft.query.filter_by(name=name).first()
    return render_template('spacecraft.html', spacecraft=spacecraft, title=name)

@universe.route('/species_all')
def species():
    """Returns all species in the database"""
    # species_all = SpeciesSchema(many=True).dump(Species.query.all())
    # return render_template('species_all.html', species_all=species_all)
    species_all = Species.query.all()
  
    return render_template('species_all.html', species_all=species_all, title='Species')

#FIXME - This route is not working at the moment
@universe.route('/species/<name>')
def species_by_name(name):
    """Returns a single species from the database"""
    species = Species.query.filter_by(name=name).first()
    return render_template('species.html', species=species, title=name)
    
@universe.route('/technologies')
def technologies():
    """Returns all technologies in the database"""
    technologies = Technology.query.all()
    return render_template('technologies.html', technologies=technologies)

@universe.route('/technologies/<name>')
def technology(name):
    """Returns a single technology from the database"""
    technology = Technology.query.filter_by(name=name).first()
    return render_template('technology.html', technology=technology, title=name)

@universe.route('/titles')
def titles():
    """Returns all titles in the database"""
    titles = Title.query.all()
    return render_template('titles.html', titles=titles)

#FIXME - This route is not working at the moment
@universe.route('/titles/<name>')
def title(name):
    """Returns a single title from the database"""
    title_ = Title.query.filter_by(name=name).first()
    return render_template('title.html', title_=title_, title=name)

@universe.route('/weapons')
def weapons():
    """Returns all weapons in the database"""
    weapons = Weapon.query.all()
    print(Weapon.query.first())
    return render_template('weapons.html', weapons=weapons)

@universe.route('/weapons/<name>')
def weapon(name):
    """Returns a single weapon from the database"""
    weapon = Weapon.query.filter_by(name=name).first()
    return render_template('weapon.html', weapon=weapon, title=name)