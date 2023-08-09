<<<<<<< HEAD
# from app.auth import auth
# from flask import render_template, abort, session, redirect, url_for, current_app
# from app.extensions import oauth
# import os
# from authlib.integrations.flask_client import OAuth
# # from authlib.common.security import generate_token
# from config import config
=======
from app.auth import auth
from flask import render_template, abort, session, redirect, url_for
from app.extensions import oauth
import os
from authlib.common.security import generate_token
from app.helpers import login_is_required
>>>>>>> stapi-models


# auth0_config = config['AUTH0']
# oauth = OAuth(current_app)

<<<<<<< HEAD
# domain = auth0_config["DOMAIN"]
# client_id = auth0_config["CLIENT_ID"]
# client_secret = auth0_config["CLIENT_SECRET"]

# oauth.register(
#     "auth0",
#     client_id=client_id,
#     client_secret=client_secret,
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f'https://{domain}/.well-known/openid-configuration'
# )

=======
>>>>>>> stapi-models

# @auth.route("/callback", methods=["GET", "POST"])
# def callback():
#     """
#     Callback redirect from Auth0
#     """
#     token = oauth.auth0.authorize_access_token()
#     session["user"] = token
#     # The app assumes for a /profile path to be available, change here if it's not
#     return redirect("/profile")
# # ************************!SECTION: Routes ************************
# @auth.route("/login")
# def login():
#     """
#     Redirects the user to the Auth0 Universal Login (https://auth0.com/docs/authenticate/login/auth0-universal-login)
#     """
#     return oauth.auth0.(
#         redirect_uri=url_for("auth.callback", _external=True)
#     )
    
# @auth.route('/profile')
# def profile():
#     """Returns the user profile"""
#     return render_template('profile.html')
# def login_is_required(function):
#     def wrapper(*args, **kwargs):
#         if "google_id" not in session:
#             abort(401)  # Unauthorized
#         else:
#             return function()
#     return wrapper


# @auth.route('/login')
# def login():
#     return render_template('login.html')


<<<<<<< HEAD
# @auth.route('/signup')
# def signup():
#     return render_template('signup.html')
=======
@auth.route('/logout')
def logout():
    
    return render_template('logout.html')
>>>>>>> stapi-models


# @auth.route('/logout')
# def logout():
#     return render_template('logout.html')


<<<<<<< HEAD
# @auth.route('/google/')
# def google():
#     # import the google client id and secret from the environment variables
#     GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
#     GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

#     CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
#     oauth.register(
#         name='google',
#         client_id=GOOGLE_CLIENT_ID,
#         client_secret=GOOGLE_CLIENT_SECRET,
#         server_metadata_url=CONF_URL,
#         client_kwargs={
#             'scope': 'openid email profile'
#         }
#     )
=======
    # Redirect to google_auth function
    redirect_uri = url_for('auth.google_auth', _external=True)
    print(redirect_uri)
    session['nonce'] = generate_token()
    # import pdb; pdb.set_trace()
    return oauth.google.authorize_redirect(redirect_uri, nonce=session['nonce'])

#FIXME - this is not working 304 error when attempting to login with google 
#NOTE - Something in relation to the redirect_uri and token and that the google client can not be found.
@auth.route('/google/auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    # user = oauth.google.parse_id_token(token)
    user = oauth.google.parse_id_token(token, nonce=session['nonce'])
    session['user'] = user
    # import pdb; pdb.set_trace()
    print(" Google User ", user)
    # return redirect('/')
    return redirect(url_for('main.profile', user=user))

>>>>>>> stapi-models

#     # Redirect to google_auth function
#     redirect_uri = url_for('auth.google_auth', _external=True)
#     print(redirect_uri)
#     session['nonce'] = generate_token()
#     import pdb; pdb.set_trace()
#     return oauth.google.authorize_redirect(redirect_uri)

# #FIXME - this is not working 304 error when attempting to login with google 
# #NOTE - Something in relation to the redirect_uri and token and that the google client can not be found.
# @auth.route('/google/auth/')
# def google_auth():
#     token = oauth.google.authorize_access_token()
#     user = oauth.google.parse_id_token(token)
#     session['user'] = user
#     import pdb; pdb.set_trace()
#     print(" Google User ", user)
#     return redirect('/')

# @auth.route('/protected_area')
# @login_is_required
# def protected_area():
#     return 'This is a protected area'
