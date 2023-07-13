from flask import Flask
import sys
import os

# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, api, oauth, ma

from config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    oauth.init_app(app)
    ma.init_app(app)

    with app.app_context():
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
    from app.users import users
    app.register_blueprint(users)
    from app.universe import universe
    app.register_blueprint(universe)
    from app.about import about
    app.register_blueprint(about)
    from app.movies import movies
    app.register_blueprint(movies)
    from app.shows import shows
    app.register_blueprint(shows)
    from app.api.resources import api_bp as api
    app.register_blueprint(api)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

                
    return app




