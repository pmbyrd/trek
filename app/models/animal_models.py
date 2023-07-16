from app.extensions import db

class Animal(db.Model):
    """Creates an instance of animal for the table in the database"""

    __tablename__ = "animals"
    
    name = db.Column(db.Text, nullable=False)
    
    uid = db.Column(db.Text, primary_key=True)
    
    earthAnimal = db.Column(db.Boolean, nullable=False) 
    
    earthInsect = db.Column(db.Boolean, nullable=False)
    
    avian = db.Column(db.Boolean, nullable=False)    
    
    canine = db.Column(db.Boolean, nullable=False)
    
    feline = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f"<Animal #{self.uid}: name = {self.name}>"
    
    def get_name(self):
        """Returns the name of the animal"""
        return self.name
    # Make a class method that will return a list of all animals that are earth animals
    @classmethod
    def get_all_earth_animals(cls):
        """Returns a list of all animals that are earth animals"""
        return cls.query.filter_by(earthAnimal=True).all()

    @classmethod
    def get_all_earth_insects(cls):
        """Returns a list of all animals that are earth insects"""
        return cls.query.filter_by(earthInsect=True).all()

    @classmethod
    def get_all_avian(cls):
        """Returns a list of all animals that are avian"""
        return cls.query.filter_by(avian=True).all()

    @classmethod
    def get_all_canine(cls):
        """Returns a list of all animals that are canine"""
        return cls.query.filter_by(canine=True).all()

    @classmethod
    def get_all_feline(cls):
        """Returns a list of all animals that are feline"""
        return cls.query.filter_by(feline=True).all()
    
    