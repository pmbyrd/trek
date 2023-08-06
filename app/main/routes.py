from app.main import bp as main
from flask import render_template, jsonify

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/lcars')
def lcars():
    return render_template('lcars-lower-decks-padd.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')

@main.route("/user_main")
def user_view():
    """
    User endpoint, can only be accessed by an authorized user
    """
    return jsonify(msg="Hello user!")

@main.route("/admin")
def admin_view():
    """
    Admin endpoint, can only be accessed by an admin
    """
    return jsonify(msg="Hello admin!")

