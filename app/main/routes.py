from app.main import bp as main
from flask import render_template, url_for

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/lcars')
def lcars():
    return render_template('lcars-lower-decks-padd.html')

@main.route('/profile')
def profile():
    """Takes the user to their profile page"""
    return render_template('profile.html')