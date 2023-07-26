from flask import Flask
import sys
import os

# Add the parent directory of the 'app' module to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.extensions import db, migrate, oauth, ma

from config import Config



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Initialize Flask extensions here
    oauth.init_app(app)

    with app.app_context():
        # NOTE- Order does matter the initialization process
        db.init_app(app)
        ma.init_app(app)
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
    from app.media import media
    app.register_blueprint(media)
    # from app.media import movies
    # app.register_blueprint(movies)
    # from app.shows import shows
    # app.register_blueprint(shows)
    from app.api import api
    app.register_blueprint(api)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

                
    return app




