"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db

DEFAULT_IMAGE_URL = "https://loading.io/icon/tpi8gu"


class User(db.Model):
    """Creates a user model for the database."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
<<<<<<< HEAD
    
    username = db.Column(db.String(32), nullable=False, unique=True)
    
    first_name= db.Column(db.String(32), nullable=False)
    
    last_name = db.Column(db.String(32), nullable=False)
    
    email = db.Column(db.String, nullable=False, unique=True)
    
    avatar = db.Column(db.String, nullable=False, default=DEFAULT_IMAGE_URL)
    
    password = db.Column(db.String, nullable=False)
    # password_hash = db.Column(db.String(64), nullable=False)
    
    bio = db.Column(db.String, nullable=True)
    
    location = db.Column(db.String, nullable=True)
=======
    username = db.Column(db.Text(32), nullable=True, unique=True)
    first_name= db.Column(db.Text(32), nullable=True)
    last_name = db.Column(db.Text(32), nullable=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    profile_pic = db.Column(db.Text, nullable=True, default=DEFAULT_IMAGE_URL)
    bio = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True)
>>>>>>> stapi-models
    
    @property
    # create a property that returns the full name of the user
    def full_name(self):
        """Returns a user's full name."""
        if self.first_name is None or self.last_name is None:
            return "Anonymous"
        else:
            full_name = f"{self.first_name} {self.last_name}"
            return full_name
    
    def __repr__(self):
        return f"<User #{self.id}: {self.username}, {self.email}>"
     

# from app.extensions import db
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash



# class User(db.Model, UserMixin):
#     """Creates a user model for the database."""
#     __tablename__ = "users"
    
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
#     username = db.Column(db.Text(32), nullable=False, unique=True)
    
#     first_name= db.Column(db.Text(32), nullable=False)
    
#     last_name = db.Column(db.Text(32), nullable=False)
    
#     email = db.Column(db.Text, nullable=False, unique=True)
    
#     avatar = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    
#     password = db.Column(db.Text, nullable=False)
#     # password_hash = db.Column(db.String(64), nullable=False)
    
#     bio = db.Column(db.Text, nullable=True)
    
#     location = db.Column(db.Text, nullable=True)
    
    
#     def __repr__(self):
#         return f"<User #{self.id}: {self.username}, {self.email}>"

#     def __init__(self, username, first_name, last_name, email, password, bio, location, avatar=None):
#         self.username = username
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.avatar = avatar or DEFAULT_IMAGE_URL
#         self.password = password
#         self.bio = bio
#         self.location = location
    
        
# #NOTE - Do no use the previous class methods when trying to implement a login system.
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)