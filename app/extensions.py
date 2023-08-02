"""

.extensions.py

This file contains the flask extensions used by the application.

Placed here in the app folder for ease of use and so other files can easily import them.

"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from authlib.integrations.flask_client import OAuth
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
oauth = OAuth()
ma = Marshmallow()
bootstrap = Bootstrap()