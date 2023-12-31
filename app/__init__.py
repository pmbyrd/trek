import sys
import json
import os
import logging
from logging.handlers import RotatingFileHandler

from click import echo
from flask import Flask, render_template
from flask.logging import default_handler

# Add the parent directory of the 'app' module to sys.path
from app.extensions import db, migrate, oauth, ma, bootstrap, db
from config import Config, config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def create_app(config_class=Config):
    app = Flask(__name__)
    #SECTION- Logging
    
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_class)
    app.secret_key = config["WEBAPP"]["SECRET_KEY"]
    # Initialize Flask extensions here
    oauth.init_app(app)
    bootstrap.init_app(app)
    configure_logging(app)
    # register_cli_commands(app)

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
    
    engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = db.inspect(engine)
    if not inspector.has_table("users"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            app.logger.info('Initialized the database!')
    else:
        app.logger.info('Database already contains the users table.')



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

def to_pretty_json(obj: dict) -> str:
    return json.dumps(obj, default=lambda o: o.__dict__, indent=4)


def page_not_found(e):
    return render_template('404.html'), 404   
# def register_cli_commands(app):
#     @app.cli.command('init_db')
#     def initialize_database():
#         """Initialize the database."""
#         db.drop_all()
#         db.create_all()
#         echo('Initialized the database!')






