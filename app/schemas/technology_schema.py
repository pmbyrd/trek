from app.extensions import ma
from app.models.star_trek_models import Technology
from flask_marshmallow.fields import URLFor, Hyperlinks

class TechnologySchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Technology
        include_fk = True
        
        _links = Hyperlinks({
          'self': URLFor('universe/technologies/<name>', values=dict(name='<name>')),
          'collection': URLFor('universe/technologies') 
        })
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()