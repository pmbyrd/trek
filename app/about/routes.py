"""Summary = This is the file for the about and informational routes."""

from flask import render_template
from app.about import about

@about.route('/')
def about_page():
    """Shows the about index page"""

    return "About Page"
