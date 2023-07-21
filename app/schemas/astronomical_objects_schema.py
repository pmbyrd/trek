from app.models.star_trek_models import AstronomicalObject
from app.extensions import ma
from flask_marshmallow.fields import URLFor, Hyperlinks

class AstronomicalObjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AstronomicalObject
        include_fk = True
        
        
        