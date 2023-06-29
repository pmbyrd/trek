"""_summary_ = This file contains the models for creating users for the application.
"""

from app.extensions import db
from flask_login import UserMixin
from flask_bcrypt import Bcrypt

class User(UserMixin, db.Model):
    __tablename__ = "user"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False, unique=True)

    def __repr__(self):
        return f"<User={self.username} id={self.id}>"
    
    
    
    @classmethod
    def signup(cls, username, email, pwd):
        """_summary_ = This method creates a new user.
        
        _params_ = username: str, email: str, pwd: str
        
        _returns_ = User object
        """
        hashed_pwd = Bcrypt().generate_password_hash(pwd).decode('utf8')
        
        user = User(
            username=username,
            email=email,
            pwd = hashed_pwd
        )
        
        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, pwd):
        """_summary_ = This method authenticates a user.
        
        _params_ = username: str, pwd: str
        
        _returns_ = User object or False
        """
        user = cls.query.filter_by(username=username).first()
        
        if user:
            is_auth = Bcrypt().check_password_hash(user.pwd, pwd)
            if is_auth:
                return user
        else:
            return False