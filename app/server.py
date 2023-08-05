import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

import http.client

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


# conn = http.client.HTTPSConnection("")

# payload = "{\"initiate_login_uri\": \"<login_url>\"}"

# headers = {
#     'content-type': "application/json",
#     'authorization': "Bearer API2_ACCESS_TOKEN",
#     'cache-control': "no-cache"
#     }

# conn.request("PATCH", "/dev-opjh6zgs54o2qcqw.us.auth0.com/api/v2/clients//nGqiiNyet5FyvNyTm3VaqDhmXIKYQnHZ", payload, headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/'
)


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/")
def home():
    return render_template("index.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))