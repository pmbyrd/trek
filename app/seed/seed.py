"""
    This file is used to the database with the data from the json files.
    
    1. Drop all tables
    2. Create all tables
    3. Use helper functions to read the json files and add the data to the database
   
"""
import json

from app.extensions import db
from app.star_trek_models import Animal, Title, Location, AstronomicalObject, Character, Performer, Element, Conflict, Weapon, Food, Technology, Company, Staff, Species, Organization, Occupation, SpacecraftClass, Spacecraft, Material, Movie, Series, Season, Episode
from app import create_app

def seed_animals():
    """Gets the json file and adds the data to the database"""
    db.drop_all()
    db.create_all()
    
    with open('app/data/animal.json') as json_file:
        data = json.load(json_file)
        for animal in data:
            animal= Animal(**animal)
            db.session.add(animal)
            db.session.commit()
            json_file.close()
    print("Animal added to database.")

def seed_astronomical_object():
    """Gets the json file and adds the astronomical object data to the database"""
    db.drop_all()
    db.create_all()
    
    with open('app/data/astronomicalObject.json') as json_file:
        data = json.load(json_file)
        for astronomicalObject in data:
            astronomicalObject = AstronomicalObject(**astronomicalObject)
            db.session.add(astronomicalObject)
            db.session.commit()
            json_file.close()
    print("Astronomical Object added to database.")
    
def seed_location():
    """Gets the json file and adds the location data to the database"""

    db.drop_all()
    db.create_all()
    
    with open('app/data/location.json') as json_file:
        data = json.load(json_file)
        for location in data:
            location = Location(**location)
            db.session.add(location)
            db.session.commit()
            json_file.close()
            
    print("Location added to database.")
    
    
def seed_character():
    """Gets the json file and adds the character data to the database"""
    db.drop_all()
    db.create_all()
    
    with open('app/data/character.json') as json_file:
        data = json.load(json_file)
        for character in data:
            character = Character(**character)
            db.session.add(character)
            db.session.commit()
            json_file.close()
    
    print("Character added to database.")




# print("Character added to database.")
        
        
# with open ('data/performer.json') as json_file:
#     data = json.load(json_file)
#     for performer in data:
#         performer = Performer(**performer)
#         db.session.add(performer)
#         db.session.commit()
#         json_file.close()

# print("Performer added to database.")
        
        
# with open('data/element.json') as json_file:
#     data = json.load(json_file)
#     for element in data:
#         element = Element(**element)
#         db.session.add(element)
#         db.session.commit()
#         json_file.close()
          
# print("Element added to database.")


# with open('data/conflict.json') as json_file:
#     data = json.load(json_file)
#     for conflict in data:
#         conflict = Conflict(**conflict)
#         db.session.add(conflict)
#         db.session.commit()
#         json_file.close()
    
# print("Conflict added to database.")


# with open('data/weapon.json') as json_file:
#     data = json.load(json_file)
#     for weapon in data:
#         weapon = Weapon(**weapon)
#         db.session.add(weapon)
#         db.session.commit()
#         json_file.close()
        
# print("Weapon added to database.")
        
        
# with open('data/food.json') as json_file:
#     data = json.load(json_file)
#     for food in data:
#         food = Food(**food)
#         db.session.add(food)
#         db.session.commit()
#         json_file.close()
        
# print("Food added to database.")


# with open('data/technology.json') as json_file:
#     data = json.load(json_file)
#     for technology in data:
#         technology = Technology(**technology)
#         db.session.add(technology)
#         db.session.commit()
#         json_file.close()
        
# print("Technology added to database.")


# with open('data/company.json') as json_file:
#     data = json.load(json_file)
#     for company in data:
#         company = Company(**company)
#         db.session.add(company)
#         db.session.commit()
#         json_file.close()
        
# print("Company added to database.")


# with open('data/staff.json') as json_file:
#     data = json.load(json_file)
#     for staff in data:
#         staff = Staff(**staff)
#         db.session.add(staff)
#         db.session.commit()
#         json_file.close()

# print("Staff added to database.")

# with open('data/species.json') as json_file:
#     data = json.load(json_file)
#     for species in data:
#         species_obj = Species(**species)
#         db.session.merge(species_obj)
#     db.session.commit()
#     json_file.close()

        
# print("Species added to database.")


# with open('data/organization.json') as json_file:
#     data = json.load(json_file)
#     for organization in data:
#         organization = Organization(**organization)
#         db.session.add(organization)
#         db.session.commit()
#         json_file.close()
        
# print("Organization added to database.")


# with open('data/occupation.json') as json_file:
#     data = json.load(json_file)
#     for occupation in data:
#         occupation = Occupation(**occupation)
#         db.session.add(occupation)
#         db.session.commit()
#         json_file.close()
        
# print("Occupation added to database.")


# with open('data/spacecraftClass.json') as json_file:
#     data = json.load(json_file)
#     for spacecraftClass in data:
#         spacecraftClass = SpacecraftClass(**spacecraftClass)
#         db.session.add(spacecraftClass)
#         db.session.commit()
#         json_file.close()
        
# print("Spacecraft Class added to database.")

   
# with open('data/spacecraft.json') as json_file:
#     data = json.load(json_file)
#     for spacecraft in data:
#         spacecraft = Spacecraft(**spacecraft)
#         db.session.add(spacecraft)
#         db.session.commit()
#         json_file.close()
        
# print('Spacecraft added to database')


# with open('data/material.json') as json_file:
#     data = json.load(json_file)
#     for material in data:
#         material = Material(**material)
#         db.session.add(material)
#         db.session.commit()
#         json_file.close()
        
# print('Material added to database')


# with open('data/movie.json') as json_file:
#     data = json.load(json_file)
#     for movie in data:
#         movie = Movie(**movie)
#         db.session.add(movie)
#         db.session.commit()
#         json_file.close()
        
# print('Movie added to database')


# with open('data/series.json') as json_file:
#     data = json.load(json_file)
#     for series in data:
#         series = Series(**series)
#         db.session.add(series)
#         db.session.commit()
#         json_file.close()

# print('Series added to database')


# with open('data/season.json') as json_file:
#     data = json.load(json_file)
#     for season in data:
#         season = Season(**season)
#         db.session.add(season)
#         db.session.commit()
#         json_file.close()


# with open('data/episode.json') as json_file:
#     data = json.load(json_file)
#     for episode in data:
#         episode = Episode(**episode)
#         db.session.add(episode)
#         db.session.commit()
#         json_file.close()

# print('Episode added to database')

# if __name__ == "__main__":
#     print ("Database populated successfully")





        



