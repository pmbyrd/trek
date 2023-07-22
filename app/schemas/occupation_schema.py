from app.extensions import ma
from app.models.star_trek_models import Occupation
from flask_marshmallow.fields import URLFor, Hyperlinks

class OccupationSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Occupation
        include_fk = True
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()