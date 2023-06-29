"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

class User(db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return f"<User={self.username} id={self.id}>"
    
#NOTE - Do no use the previous class methods when trying to implement a login system.
    
