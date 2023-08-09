"""Summary: Model for making a comment on movie or show."""

from app.extensions import db
from datetime import datetime
# FIXME: Need to make a relationship between the user and the comment.


class Comment(db.Model):
    """Parent class for comments."""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # need a rating out of 10
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    


# Make a parent class and distinguish between movie and show comments.