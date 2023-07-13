from app.auth import auth
from flask import render_template, abort, session, redirect, url_for
from app.extensions import oauth


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            abort(401)  # Unauthorized
        else:
            return function()
    return wrapper


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
def logout():
    return render_template('logout.html')


@auth.route('/google/')
def google():

    GOOGLE_CLIENT_ID = 'YOUR GOOGLE CLIENT ID'
    GOOGLE_CLIENT_SECRET = 'YOUR GOOGLE CLIENT SECRET'

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('auth.google_auth', _external=True)
    print(redirect_uri)
    return oauth.google.authorize_redirect(redirect_uri)


@auth.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    user = oauth.google.parse_id_token(token)
    print(" Google User ", user)
    return redirect('/')

@auth.route('/protected_area')
@login_is_required
def protected_area():
    return 'This is a protected area'
