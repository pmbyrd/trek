"""Summary: Creates an animal schema class that can marshall the data from the backend to the frontend
"""
from app.extensions import ma
from app.models.star_trek_models import Animal
from flask_marshmallow.fields import URLFor, Hyperlinks


class AnimalSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # The fields to be exposed
        model = Animal
        include_fk = True

        _links = Hyperlinks({
            'self': {
                'href': URLFor('universe.api_animals',
                               values=dict(id='<id>')),
                'title': 'The animal'
            }
                
        })
