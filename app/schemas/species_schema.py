from app.extensions import ma
from app.models.star_trek_models import Species
from flask_marshmallow.fields import URLFor, Hyperlinks

class SpeciesSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Species
        include_fk = True
        
        _links = Hyperlinks({
          'self': URLFor('universe/species/<name>', values=dict(name='<name>')),
          'collection': URLFor('universe/species') 
        })
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()