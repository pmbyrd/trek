import cli
from app import create_app
from app.extensions import db
from app.models import User
from app.star_trek_models import (
    AstronomicalObject, 
    Animal,
    Character,
    Element,
    Location,
    Performer,
    Season,
    Episode,
    Series,
    Spacecraft,
    SpacecraftClass,
    Staff,
    Material,
    Conflict,
    Food,
    Technology,
    Company,
    Occupation,
    Species,
    Title,
    Weapon
    )
app = create_app()
# Register the custom commands with the application
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    """Makes a shell context that adds the database instance and models to the shell session."""
    return {
        'db': db,
        'AstronomicalObject': AstronomicalObject,
        'Animal': Animal,
        'Character': Character,
        'Element': Element,
        'Location': Location,
        'Performer': Performer,
        'Season': Season,
        'Episode': Episode,
        'Series': Series,
        'Spacecraft': Spacecraft,
        'SpacecraftClass': SpacecraftClass,
        'Staff': Staff,
        'Material': Material,
        'Conflict': Conflict,
        'Food': Food,
        'Technology': Technology,
        'Company': Company,
        'Occupation': Occupation,
        'Species': Species,
        'Title': Title,
        'Weapon': Weapon
    }

if __name__ == '__main__':
    print('Running the application.')
    