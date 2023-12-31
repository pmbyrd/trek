"""
    This file is used to the database with the data from the json files.
    
    1. Drop all tables
    2. Create all tables
    3. Use helper functions to read the json files and add the data to the database
   
"""
import json

from app.extensions import db
from app.models.star_trek_models import Title, Location, AstronomicalObject, Character, Performer, Element, Conflict, Weapon, Food, Technology, Company, Staff, Species, Organization, Occupation, SpacecraftClass, Spacecraft, Material, Movie, Series, Season, Episode
from app.models.animal_models import Animal
from app import create_app


#NOTE I am currently dropping all tables with creating new ones. This is not ideal for production.



def seed_animals():
    """Gets the JSON file and adds the data to the database"""
    try:
        with open('app/data/animal.json') as json_file:
            data = json.load(json_file)
            for animal_data in data:
                existing_animal = Animal.query.filter_by(uid=animal_data['uid']).first()
                if existing_animal:
                    continue  # Skip insertion if the record already exists
                else:
                    animal = Animal(**animal_data)
                    db.session.add(animal)
                    db.session.commit()

        print("Animal data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding animals: {e}")


def seed_astronomical_object():
    """Gets the JSON file and adds the data to the database"""
    try:
        with open('app/data/astronomicalObject.json') as json_file:
            data = json.load(json_file)
            for astronomicalObject_data in data:
                existing_astronomicalObject = AstronomicalObject.query.filter_by(uid=astronomicalObject_data['uid']).first()
                if existing_astronomicalObject:
                    continue  # Skip insertion if the record already exists
                else:
                    astronomicalObject = AstronomicalObject(**astronomicalObject_data)
                    db.session.add(astronomicalObject)
                    db.session.commit()

        print("Astronomical Object data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding astronomical objects: {e}")

def seed_location():
    """Gets the JSON file and adds the location data to the database"""
    try:
        with open('app/data/location.json') as json_file:
            data = json.load(json_file)
            for location_data in data:
                location = Location(**location_data)
                db.session.add(location)
                db.session.commit()

        print("Location data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding locations: {e}")

    
def seed_character():
    """Gets the JSON file and adds the character data to the database"""
    try:
        with open('app/data/character.json') as json_file:
            data = json.load(json_file)
            for character_data in data:
                existing_character = Character.query.filter_by(uid=character_data['uid']).first()
                if existing_character:
                    continue  # Skip insertion if the record already exists
                else:
                    character = Character(**character_data)
                    db.session.add(character)
                    db.session.commit()

        print("Character data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding characters: {e}")


def seed_performer():
    """Gets the JSON file and adds the performer data to the database"""
    try:
        with open('app/data/performer.json') as json_file:
            data = json.load(json_file)
            for performer_data in data:
                existing_performer = Performer.query.filter_by(uid=performer_data['uid']).first()
                if existing_performer:
                    continue  # Skip insertion if the record already exists
                else:
                    performer = Performer(**performer_data)
                    db.session.add(performer)
                    db.session.commit()

        print("Performer data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding performers: {e}")



def seed_element():
    """Gets the JSON file and adds the element data to the database"""
    try:
        with open('app/data/element.json') as json_file:
            data = json.load(json_file)
            for element_data in data:
                existing_element = Element.query.filter_by(uid=element_data['uid']).first()
                if existing_element:
                    continue  # Skip insertion if the record already exists
                else:
                    element = Element(**element_data)
                    db.session.add(element)
                    db.session.commit()

        print("Element data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding elements: {e}")

       
        
def seed_conflict():
    """Gets the JSON file and adds the conflict data to the database"""
    try:
        with open('app/data/conflict.json') as json_file:
            data = json.load(json_file)
            for conflict_data in data:
                existing_conflict = Conflict.query.filter_by(uid=conflict_data['uid']).first()
                if existing_conflict:
                    continue  # Skip insertion if the record already exists
                else:
                    conflict = Conflict(**conflict_data)
                    db.session.add(conflict)
                    db.session.commit()

        print("Conflict data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding conflicts: {e}")

    
    
def seed_weapon():
    """Gets the JSON file and adds the weapon data to the database"""
    try:
        with open('app/data/weapon.json') as json_file:
            data = json.load(json_file)
            for weapon_data in data:
                existing_weapon = Weapon.query.filter_by(uid=weapon_data['uid']).first()
                if existing_weapon:
                    continue  # Skip insertion if the record already exists
                else:
                    weapon = Weapon(**weapon_data)
                    db.session.add(weapon)
                    db.session.commit()

        print("Weapon data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding weapons: {e}")

    
def seed_food():
    """Gets the JSON file and adds the food data to the database"""
    try:
        with open('app/data/food.json') as json_file:
            data = json.load(json_file)
            for food_data in data:
                existing_food = Food.query.filter_by(uid=food_data['uid']).first()
                if existing_food:
                    continue  # Skip insertion if the record already exists
                else:
                    food = Food(**food_data)
                    db.session.add(food)
                    db.session.commit()

        print("Food data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding food: {e}")


def seed_technology():
    """Gets the JSON file and adds the technology data to the database"""
    try:
        with open('app/data/technology.json') as json_file:
            data = json.load(json_file)
            for technology_data in data:
                existing_technology = Technology.query.filter_by(uid=technology_data['uid']).first()
                if existing_technology:
                    continue  # Skip insertion if the record already exists
                else:
                    technology = Technology(**technology_data)
                    db.session.add(technology)
                    db.session.commit()

        print("Technology data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding technology: {e}")

def seed_company():
    """Gets the JSON file and adds the company data to the database"""
    try:
        with open('app/data/company.json') as json_file:
            data = json.load(json_file)
            for company_data in data:
                existing_company = Company.query.filter_by(uid=company_data['uid']).first()
                if existing_company:
                    continue  # Skip insertion if the record already exists
                else:
                    company = Company(**company_data)
                    db.session.add(company)
                    db.session.commit()

        print("Company data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding companies: {e}")


def seed_staff():
    """Gets the JSON file and adds the staff data to the database"""
    try:
        with open('app/data/staff.json') as json_file:
            data = json.load(json_file)
            for staff_data in data:
                existing_staff = Staff.query.filter_by(uid=staff_data['uid']).first()
                if existing_staff:
                    continue  # Skip insertion if the record already exists
                else:
                    staff = Staff(**staff_data)
                    db.session.add(staff)
                    db.session.commit()

        print("Staff data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding staff: {e}")

def seed_species():
    """Gets the JSON file and adds the species data to the database"""
    try:
        with open('app/data/species.json') as json_file:
            data = json.load(json_file)
            for species_data in data:
                existing_species = Species.query.filter_by(uid=species_data['uid']).first()
                if existing_species:
                    continue  # Skip insertion if the record already exists
                else:
                    species = Species(**species_data)
                    db.session.add(species)
                    db.session.commit()

        print("Species data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding species: {e}")


def seed_organization():
    """Gets the JSON file and adds the organization data to the database"""
    try:
        with open('app/data/organization.json') as json_file:
            data = json.load(json_file)
            for organization_data in data:
                existing_organization = Organization.query.filter_by(uid=organization_data['uid']).first()
                if existing_organization:
                    continue  # Skip insertion if the record already exists
                else:
                    organization = Organization(**organization_data)
                    db.session.add(organization)
                    db.session.commit()

        print("Organization data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding organizations: {e}")



def seed_occupation():
    """Gets the JSON file and adds the occupation data to the database"""
    try:
        with open('app/data/occupation.json') as json_file:
            data = json.load(json_file)
            for occupation_data in data:
                existing_occupation = Occupation.query.filter_by(uid=occupation_data['uid']).first()
                if existing_occupation:
                    continue  # Skip insertion if the record already exists
                else:
                    occupation = Occupation(**occupation_data)
                    db.session.add(occupation)
                    db.session.commit()

        print("Occupation data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding occupations: {e}")


def seed_spacecraft():
    """Gets the JSON file and adds the spacecraft data to the database"""
    try:
        with open('app/data/spacecraft.json') as json_file:
            data = json.load(json_file)
            for spacecraft_data in data:
                existing_spacecraft = Spacecraft.query.filter_by(uid=spacecraft_data['uid']).first()
                if existing_spacecraft:
                    continue  # Skip insertion if the record already exists
                else:
                    spacecraft = Spacecraft(**spacecraft_data)
                    db.session.add(spacecraft)
                    db.session.commit()

        print("Spacecraft data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding spacecraft: {e}")




def seed_spacecraft_class():
    """Gets the JSON file and adds the spacecraft class data to the database"""
    try:
        with open('app/data/spacecraftClass.json') as json_file:
            data = json.load(json_file)
            for spacecraft_class_data in data:
                existing_spacecraft_class = SpacecraftClass.query.filter_by(uid=spacecraft_class_data['uid']).first()
                if existing_spacecraft_class:
                    continue  # Skip insertion if the record already exists
                else:
                    spacecraft_class = SpacecraftClass(**spacecraft_class_data)
                    db.session.add(spacecraft_class)
                    db.session.commit()

        print("Spacecraft Class data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding spacecraft classes: {e}")


def seed_material():
    """Gets the JSON file and adds the material data to the database"""
    try:
        with open('app/data/material.json') as json_file:
            data = json.load(json_file)
            for material_data in data:
                existing_material = Material.query.filter_by(uid=material_data['uid']).first()
                if existing_material:
                    continue  # Skip insertion if the record already exists
                else:
                    material = Material(**material_data)
                    db.session.add(material)
                    db.session.commit()

        print("Material data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding materials: {e}")



def seed_movie():
    """Gets the JSON file and adds the movie data to the database"""
    try:
        with open('app/data/movie.json') as json_file:
            data = json.load(json_file)
            for movie_data in data:
                existing_movie = Movie.query.filter_by(uid=movie_data['uid']).first()
                if existing_movie:
                    continue  # Skip insertion if the record already exists
                else:
                    movie = Movie(**movie_data)
                    db.session.add(movie)
                    db.session.commit()

        print("Movie data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding movies: {e}")



def seed_series():
    """Gets the JSON file and adds the series data to the database"""
    try:
        with open('app/data/series.json') as json_file:
            data = json.load(json_file)
            for series_data in data:
                existing_series = Series.query.filter_by(uid=series_data['uid']).first()
                if existing_series:
                    continue  # Skip insertion if the record already exists
                else:
                    series = Series(**series_data)
                    db.session.add(series)
                    db.session.commit()

        print("Series data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding series: {e}")


def seed_season():
    """Gets the JSON file and adds the season data to the database"""
    try:
        with open('app/data/season.json') as json_file:
            data = json.load(json_file)
            for season_data in data:
                existing_season = Season.query.filter_by(uid=season_data['uid']).first()
                if existing_season:
                    continue  # Skip insertion if the record already exists
                else:
                    season = Season(**season_data)
                    db.session.add(season)
                    db.session.commit()

        print("Season data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding seasons: {e}")


def seed_episode():
    """Gets the JSON file and adds the episode data to the database"""
    try:
        with open('app/data/episode.json') as json_file:
            data = json.load(json_file)
            for episode_data in data:
                existing_episode = Episode.query.filter_by(uid=episode_data['uid']).first()
                if existing_episode:
                    continue  # Skip insertion if the record already exists
                else:
                    episode = Episode(**episode_data)
                    db.session.add(episode)
                    db.session.commit()

        print("Episode data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding episodes: {e}")


def seed_title():
    """Gets the JSON file and adds the title data to the database"""
    try:
        with open('app/data/title.json') as json_file:
            data = json.load(json_file)
            for title_data in data:
                existing_title = Title.query.filter_by(uid=title_data['uid']).first()
                if existing_title:
                    continue  # Skip insertion if the record already exists
                else:
                    title = Title(**title_data)
                    db.session.add(title)
                    db.session.commit()

        print("Title data added to the database.")
    except Exception as e:
        print(f"Error occurred while seeding titles: {e}")







        



