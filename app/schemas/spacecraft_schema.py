from app.extensions import ma
from app.models.star_trek_models import Spacecraft
from flask_marshmallow.fields import URLFor, Hyperlinks

class SpacecraftSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Spacecraft
        include_fk = True
        
        _links = Hyperlinks({
          'self': URLFor('universe/spacescrafts/<name>', values=dict(name='<name>')),
          'collection': URLFor('universe/spacescrafts') 
        })
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()