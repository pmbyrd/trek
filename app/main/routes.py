from app.main import bp as main
from flask import render_template, session, abort
from app.helpers import login_is_required
from app.models.models import User

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/lcars')
def lcars():
    return render_template('lcars-lower-decks-padd.html')


@login_is_required
@main.route('/profile')
def profile():
    """Takes the user to their profile page"""
    # need to test that the user is logged in
    user = session.get('user')
    if user is None:
        return abort(401)
    else:
        print(user)
    
    return render_template('profile.html', user=user)