from app.extensions import ma
from app.models.star_trek_models import Organization

class OrganizationSchema(ma.SQLAlchemyAutoSchema):
    class meta:
        model = Organization
        include_fk = True
        
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.fields = None
            self.load_only = ()
            self.dump_only = ()
            self.exclude = ()
            self.additional = ()