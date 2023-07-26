"""Summary = This page initializes the shows blueprint."""

from flask import Blueprint

shows = Blueprint(
    'shows', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/shows'
    )

from app.media import routes