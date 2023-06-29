"""_summary_ = This file contains the routes for the posts blueprint.
"""

from flask import render_template
from app.posts import posts

@posts.route('/')
def show_posts():
    return "Posts"