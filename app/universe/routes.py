"""Summary: This file contains the routes for the universe blueprint.
"""

# Make sure to import the blueprint
from flask import jsonify
from app.universe import universe
from flask import render_template, jsonify, request
from app.models.animal_models import Animal
from app.schemas.animal_schema import AnimalSchema
from app.helpers import MemoryAlphaScraper, replace_space


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
    animals = Animal.query.all()
    categories = {
        'canines': Animal.get_all_canine(),
        'felines': Animal.get_all_feline(),
        'earth_animals': Animal.get_all_earth_animals(),
        'earth_insects': Animal.get_all_earth_insects(),
        'avians': Animal.get_all_avian()
    }

    random_animal_names_sample = [animal.name for category_animals in categories.values(
    ) for animal in category_animals[:5]]

    scrapped_animals = []
    print(random_animal_names_sample)
    try:
        for name in random_animal_names_sample:
            print(name)
            formatted_name = replace_space(name)
            print(formatted_name)
            souped_animal = MemoryAlphaScraper(formatted_name)
            images = MemoryAlphaScraper.get_images(souped_animal)
            content = MemoryAlphaScraper.get_content(souped_animal)

            scrapped_animal = {
                'name': name,
                'images': images,
                'content': content
            }

            scrapped_animals.append(scrapped_animal)
    except AttributeError as e:
        print(e)
        pass

    return jsonify(random_animal_names_sample, scrapped_animals)



@universe.route('/animals/results', methods=['GET', 'POST'])
def animal_results():
    """Returns a single animal from the database"""
    # gets the animals from the front end that needed images to be scraped via beautiful soup
    response = request.get_json()
    # extract the
    print(response["data"])

    return jsonify(response)
