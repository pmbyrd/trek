"""_summary_ = This file contains the routes for the users of the application.
"""

from flask import render_template, url_for, redirect
from app.users import users
from app.models.models import User
from app.extensions import db

@users.route('/')
def users_page():
    # list 10 users
    users = User.query.limit(10).all()
    return render_template('users.html', users=users)


