from app.extensions import db
from app.models.models import User
from app.media.models.review_model import Review
from app.models.star_trek_models import Movie
from json_trek import JSONTrek

trek = JSONTrek()

def generate_fake_reviews():
    for movie in trek.movies:
        # Handle a 