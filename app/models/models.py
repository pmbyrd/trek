"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"


class User(db.Model, UserMixin):
    """Creates a user model for the database."""
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String(32), nullable=False, unique=True)
    
    first_name= db.Column(db.String(32), nullable=False)
    
    last_name = db.Column(db.String(32), nullable=False)
    
    email = db.Column(db.String, nullable=False, unique=True)
    
    avatar = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)
    
    password = db.Column(db.String, nullable=False)
    # password_hash = db.Column(db.String(64), nullable=False)
    
    bio = db.Column(db.String, nullable=True)
    
    location = db.Column(db.String, nullable=True)
    
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"

    def __init__(self, username, first_name, last_name, email, password, bio, location, avatar=None):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.avatar = avatar or DEFAULT_IMAGE_URL
        self.password = password
        self.bio = bio
        self.location = location
    
        
#NOTE - Do no use the previous class methods when trying to implement a login system.
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)