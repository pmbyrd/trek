from app.models.star_trek_models import Character
from flask_marshmallow.fields import URLFor, Hyperlinks
from app.extensions import ma

class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Character
        include_fk = True
        
        _links = Hyperlinks({
            'self': {
                'href': URLFor('universe.api_characters',
                               values=dict(id='<id>')),
                'title': 'The character'
            }
        })
    
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()