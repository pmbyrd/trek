"""Summary = This is the about blueprint. It defines the about page.
"""

from flask import Blueprint

about = Blueprint(
    'about', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/about'
    
    )

from app.about import routes