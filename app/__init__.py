from flask import Flask
import sys
import os

# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, seeder

from config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main
    app.register_blueprint(main)
    from app.auth import auth
    app.register_blueprint(auth)
    from app.posts import posts
    app.register_blueprint(posts)
    from app.users import users
    app.register_blueprint(users)
    from app.quadrants import quadrants
    app.register_blueprint(quadrants)
    from app.about import about
    app.register_blueprint(about)
    from app.movies import movies
    app.register_blueprint(movies)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    
    
    @app.cli.command('init-db')
    def init_db():
        """Initialize the database."""
        with app.app_context():
            print('Initialized the database.') 
            
    @app.cli.command('print-db')
    def print_db():
        """Shows the database."""
        print(db)
        
    @app.cli.command('seed-db')
    def seed_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.users_seed import seed_db
                seed_db()
                print('Seeded the database.')
    
    @app.cli.command('seed-trek-animal-db')
    def seed_trek_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_animals
                seed_animals()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-astronomical-object-db')
    def seed_trek_astronomical_object_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_astronomical_object
                seed_astronomical_object()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-location-db')
    def seed_trek_location_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_location
                seed_location()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-character-db')
    def seed_trek_character_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_character
                seed_character()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-performer-db')
    def seed_trek_performer_db():            
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_performer
                seed_performer()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-element-db')
    def seed_trek_element_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_element
                seed_element()
                print('Seeded the database.')
    
    @app.cli.command('seed-trek-conflict-db')
    def seed_trek_conflict_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_conflict
                seed_conflict()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-weapons-db')
    def seed_trek_weapon_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_weapon
                seed_weapon()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-food-db')
    def seed_trek_food_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_food
                seed_food()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-technology-db')
    def seed_trek_technology_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_technology
                seed_technology()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-company-db')
    def seed_trek_company_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_company
                seed_company()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-staff-db')
    def seed_trek_staff_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_staff
                seed_staff()
                print('Seeded the database.')
                
    ##########TODO - There maybe an error in the species seed file
    ########## !all data may not be seeding           
    @app.cli.command('seed-trek-species-db')
    def seed_trek_species_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_species
                seed_species()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-organization-db')
    def seed_trek_organization_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_organization
                seed_organization()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-occupation-db')
    def seed_trek_occupation_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_occupation
                seed_occupation()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-spacecraft-db')
    def seed_trek_spacecraft_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_spacecraft
                seed_spacecraft()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-material-db')
    def seed_trek_material_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_material
                seed_material()
                print('Seeded the database.')
  
    @app.cli.command('seed-trek-movie-db')
    def seed_trek_movie_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_movie
                seed_movie()
                print('Seeded the database.')
     
    @app.cli.command('seed-trek-series-db')
    def seed_trek_series_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_series
                seed_series()
                print('Seeded the database.')           
    
    @app.cli.command('seed-trek-season-db')
    def seed_trek_season_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_season
                seed_season()
                print('Seeded the database.')
        
    @app.cli.command('seed-trek-episode-db')
    def seed_trek_episode_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_episode
                seed_episode()
                print('Seeded the database.')
                
    @app.cli.command('seed-trek-title-db')
    def seed_trek_title_db():
        """Adds seed data to the database."""
        with app.app_context():
            if app.config['ENV'] == 'development':
                from app.seed.seed import seed_title
                seed_title()
                print('Seeded the database.')
                
    @app.cli.command('drop-db')
    def drop_db():
        """Drops the database."""
        with app.app_context():
            db.drop_all()
            print('Dropped the database.')           
    
    
    
    return app

