"""_summary_ = This file initializes the posts blueprint.
"""

from flask import Blueprint
from app.extensions import db

posts = Blueprint(
    "posts", __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/posts"   
)

from app.posts import routes