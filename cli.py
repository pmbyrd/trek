"""Summary: This file helps to define custom commands for the flask application.
"""

import os
import click
from app.extensions import db   
from app import create_app
app = create_app()
# Register the custom commands with the application
def register(app):
    @app.cli.group()
    def custom_db():
        """Custom database commands."""
        pass
    
    @custom_db.command("create")
    def create_db():
        """Create the database."""
        db.create_all()
        print('Database created.')
        
    @custom_db.command("drop")
    def drop_db():
        """Drop the database."""
        db.drop_all()
        print('Database dropped.')
        
    @custom_db.command("print")
    def print_db():
        """Print the database."""
        print(db)
        
    @custom_db.command("init")
    def init_db():
        """Initialize the database."""
        db.create_all()
        print('Database initialized.')
    
    @app.cli.group()
    def seed_db():
        """Seed the database."""
        pass
    
    @seed_db.command("animal")
    def seed_animal():
        """Seed the animal table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_animals
                seed_animals()
                print('Seeded the database.')
    
    @seed_db.command("astronomical")
    def seed_astronomical_object():
        """Seed the astronomical_object table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_astronomical_object
                seed_astronomical_object()
                print('Seeded the database.')
                
    @seed_db.command("location")
    def seed_location():
        """Seed the location table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_location
                seed_location()
                print('Seeded the database.')
                
    @seed_db.command("character")
    def seed_character():
        """Seed the character table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_character
                seed_character()
                print('Seeded the database.')
                
    @seed_db.command("performer")
    def seed_performer():
        """Seed the performer table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_performer
                seed_performer()
                print('Seeded the database.')

    @seed_db.command("element")
    def seed_element():
        """Seed the element table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_element
                seed_element()
                print('Seeded the database.')
                
    @seed_db.command("conflict")
    def seed_conflict():
        """Seed the conflict table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_conflict
                seed_conflict()
                print('Seeded the database.')
                
    
    @seed_db.command("weapon")
    def seed_weapon():
        """Seed the weapon table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_weapon
                seed_weapon()
                print('Seeded the database.')
                
    @seed_db.command("food")
    def seed_food():
        """Seed the food table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_food
                seed_food()
                print('Seeded the database.')
    
    @seed_db.command("technology")
    def seed_technology():
        """Seed the technology table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_technology
                seed_technology()
                print('Seeded the database.')
    
    @seed_db.command("company")
    def seed_company():
        """Seed the company table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_company
                seed_company()
                print('Seeded the database.')
  

    @seed_db.command("staff")
    def seed_staff():
        """Seed the staff table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_staff
                seed_staff()
                print('Seeded the database.')
  
    
    @seed_db.command("species")
    def seed_species():
        """Seed the species table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_species
                seed_species()
                print('Seeded the database.')    
    
    
    @seed_db.command("organization")
    def seed_organization():
        """Seed the organization table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_organization
                seed_organization()
                print('Seeded the database.')  
                
    
    @seed_db.command("occupation")
    def seed_occupation():
        """Seed the occupation table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_occupation
                seed_occupation()
                print('Seeded the database.')              
                
    @seed_db.command("spacecraft")
    def seed_spacecraft():
        """Seed the spacecraft table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_spacecraft
                seed_spacecraft()
                print('Seeded the database.')
                
    @seed_db.command("spacecraft-class")
    def seed_spacecraft_class():
        """Seed the spacecraftClass table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_spacecraft_class
                seed_spacecraft_class()
                print('Seeded the database.')
                
    
    @seed_db.command("material")
    def seed_material():
        """Seed the material table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_material
                seed_material()
                print('Seeded the database.')
                
    @seed_db.command("movie")
    def seed_movie():
        """Seed the movie table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_movie
                seed_movie()
                print('Seeded the database.')
                
    @seed_db.command("series")
    def seed_series():
        """Seed the series table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_series
                seed_series()
                print('Seeded the database.')
                
    @seed_db.command("season")
    def seed_season():
        """Seed the season table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_season
                seed_season()
                print('Seeded the database.')
                
    @seed_db.command("episode")
    def seed_episode():
        """Seed the episode table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_episode
                seed_episode()
                print('Seeded the database.')
                
    
    @seed_db.command("title")
    def seed_title():
        """Seed the title table."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_title
                seed_title()
                print('Seeded the database.')
                
                
    