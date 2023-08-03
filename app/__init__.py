import sys
import os
import logging
from logging.handlers import RotatingFileHandler

from click import echo
from flask import Flask
from flask.logging import default_handler

# Add the parent directory of the 'app' module to sys.path
from app.extensions import db, migrate, oauth, ma, bootstrap
from config import Config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def create_app(config_class=Config):
    app = Flask(__name__)
    #SECTION- Logging
    
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_class)
    # Initialize Flask extensions here
    oauth.init_app(app)
    bootstrap.init_app(app)
    configure_logging(app)

    with app.app_context():
        # NOTE- Order does matter the initialization process
        db.init_app(app)
        ma.init_app(app)
    migrate.init_app(app, db)
    
#     if app.config['LOG_WITH_GUNICORN']:
#     gunicorn_error_logger = logging.getLogger('gunicorn.error')
#     app.logger.handlers.extend(gunicorn_error_logger.handlers)
#     app.logger.setLevel(logging.DEBUG)
# else:
#     ... standard logging configuration ...

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

def configure_logging(app):
    # Logging Configuration
    if app.config['LOG_WITH_GUNICORN']:
        gunicorn_error_logger = logging.getLogger('gunicorn.error')
        app.logger.handlers.extend(gunicorn_error_logger.handlers)
        app.logger.setLevel(logging.DEBUG)
    else:
        file_handler = RotatingFileHandler('instance/flask-user-management.log',
                                           maxBytes=16384,
                                           backupCount=20)
        file_formatter = logging.Formatter('%(asctime)s %(levelname)s %(threadName)s-%(thread)d: %(message)s [in %(filename)s:%(lineno)d]')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

    # Remove the default logger configured by Flask
    app.logger.removeHandler(default_handler)

    app.logger.info('Starting the Flask User Management App...')





