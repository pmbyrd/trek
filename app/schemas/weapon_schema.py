from app.extensions import ma
from app.models.star_trek_models import Weapon
from flask_marshmallow.fields import URLFor, Hyperlinks

class WeaponSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Weapon
        include_fk = True
        
        _links = Hyperlinks({
          'self': URLFor('universe/weapons/<name>', values=dict(name='<name>')),
          'collection': URLFor('universe/weapons') 
        })
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()