import os


# Determine the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
    # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
    # update the URI to the postgres database to use the supported 'postgresql://' scheme
    if os.getenv('DATABASE_URL'):
        SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
    else:
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Logging
    LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
    WTF_CSRF_ENABLED = False
# import os
# from dotenv import load_dotenv
# import psycopg2
# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config(object):
#     SECRET_KEY = os.environ.get('SECRET_KEY')
#     OMDB_API_KEY = os.environ.get('OMDB_API_KEY')       
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
    #     or 'sqlite:///' + os.path.join(basedir, 'app.db') or 'postgresql:///trek'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    
#     #assign the database URI to the SQLALCHEMY_DATABASE_URI key
# class ProductionConfig(Config):
#     DATABASE_URI = 'mysql://user@localhost/foo'

# class DevelopmentConfig(Config):
#     DATABASE_URI = "sqlite:////tmp/foo.db"

# class TestingConfig(Config):
#     DATABASE_URI = 'sqlite:///trek.db'
#     TESTING = True