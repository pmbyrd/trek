from app.extensions import ma
from app.models.star_trek_models import SpacecraftClass
from flask_marshmallow.fields import URLFor, Hyperlinks

class SpacecraftClassSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = SpacecraftClass
        include_fk = True
        
        _links = Hyperlinks({
          'self': URLFor('universe/spacescraft-classes/<name>', values=dict(name='<name>')),
          'collection': URLFor('universe/spacescraft-classes') 
        })
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()