"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"


class User(db.Model):
    """Creates a user model for the database."""
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.Text, nullable=False, unique=True)
    
    first_name= db.Column(db.Text, nullable=False)
    
    last_name = db.Column(db.Text, nullable=False)
    
    email = db.Column(db.Text, nullable=False, unique=True)
    
    image = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
    password = db.Column(db.Text, nullable=False)
    
    bio = db.Column(db.Text, nullable=True)
    
    location = db.Column(db.Text, nullable=True)
    
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    def __init__(self, username, first_name, last_name, email, password, bio, location, created_at, image=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.image = image or DEFAULT_IMAGE_URL
        self.password = password
        self.bio = bio
        self.location = location
#NOTE - Do no use the previous class methods when trying to implement a login system.
    
