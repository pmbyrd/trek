from flask import Flask
import sys
import os

# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate

from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask extensions here

    # Register blueprints here
    from app.main import bp as main
    app.register_blueprint(main)
    from app.auth import auth
    app.register_blueprint(auth)
    from app.posts import posts
    app.register_blueprint(posts)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    
    @app.cli.command('init-db')
    def init_db():
        """Initialize the database."""
        with app.app_context():
            db.create_all()
        print('Initialized the database.')  
    
    return app

