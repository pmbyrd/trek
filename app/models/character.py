from app.extensions import db

class Character(db.Model):
    """Creates an instance of a character for the database."""
    
    __tablename__ = "characters"
    
    uid = db.Column(db.Text, primary_key=True)
    
    name = db.Column(db.Text, nullable=False)
    
    gender = db.Column(db.Text, nullable=True)
    
    yearOfBirth = db.Column(db.Integer, nullable=True)
    
    monthOfBirth = db.Column(db.Integer, nullable=True)
    
    dayOfBirth = db.Column(db.Integer, nullable=True)
    
    placeOfBirth = db.Column(db.Text, nullable=True)
    
    yearOfDeath = db.Column(db.Integer, nullable=True)
    
    monthOfDeath = db.Column(db.Integer, nullable=True)
    
    dayOfDeath = db.Column(db.Integer, nullable=True)
    
    placeOfDeath = db.Column(db.Text, nullable=True)
    
    height = db.Column(db.Integer, nullable=True)
    
    weight = db.Column(db.Integer, nullable=True)
    
    deceased = db.Column(db.Boolean, nullable=True)
    
    bloodType = db.Column(db.Text, nullable=True)
    
    maritalStatus= db.Column(db.Text, nullable=True)
    
    serialNumber = db.Column(db.Text, nullable=True)
    
    hologramActivationDate = db.Column(db.Integer, nullable=True)
    
    hologramStatus = db.Column(db.Text, nullable=True)
    
    hologram = db.Column(db.Boolean, nullable=True)
    
    fictionalCharacter = db.Column(db.Boolean, nullable=True)
    
    mirror = db.Column(db.Boolean, nullable=True)
    
    alternateReality = db.Column(db.Boolean, nullable=True)
    
    hologramDateStatus = db.Column(db.Integer, nullable=True)
    
    def __repr__(self):
        return f"<Character #{self.uid}: name = {self.name}>"
    
    