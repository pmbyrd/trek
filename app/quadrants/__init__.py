"""summary: This file initializes the quadrants blueprint.
    Quandrants data will include but not limited to the following:
    - Location
    - Character
    - Animals
    - Species
    - Element
    - Conflict
    - Weapon
    - Ships
"""

from flask import Blueprint

quadrants = Blueprint(
    'quadrants', __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/quadrants'   
)

from app.quadrants import routes