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
    # @app.cli.command('seed-trek-title-db')
    # def seed_trek_titles():
    #     """Adds seed data to the database."""
    #     with app.app_context():
    #         if app.config['ENV'] == 'development':
    #             from app.seed.seed import seed_title
    #             seed_title()
    #             print('Seeded the database.')
                
    @app.cli.command('drop-db')
    def drop_db():
        """Drops the database."""
        with app.app_context():
            db.drop_all()
            print('Dropped the database.')           
    
    
    
    return app

