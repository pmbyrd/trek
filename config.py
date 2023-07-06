import os
from dotenv import load_dotenv
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    OMDB_API_KEY = os.environ.get('OMDB_API_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db') or 'postgresql:///trek'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    #assign the database URI to the SQLALCHEMY_DATABASE_URI key
