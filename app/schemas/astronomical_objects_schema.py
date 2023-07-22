from app.models.star_trek_models import AstronomicalObject
from app.extensions import ma
from flask_marshmallow.fields import URLFor, Hyperlinks

class AstronomicalObjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AstronomicalObject
        include_fk = True
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()
        
        
        