from marshmallow import Schema, fields

# Define the Marshmallow schema for the Movie class
class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    release_year = fields.Int()