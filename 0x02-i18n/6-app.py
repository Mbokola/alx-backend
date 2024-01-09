#!/usr/bin/env python3
""" 0-app module
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
# instantiate the Babel object in your app.
babel = Babel(app)


class Config:
    """ configure available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# set Config as config for your Flask app.
app.config.from_object(Config)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    """ Locale selector
    """
    user_preferred_language = request.args.get('locale', None)
    user = g.user
    if user:
        return users["locale"]
    if user_preferred_language and user_preferred_language in Config.LANGUAGES:
        return user_preferred_language
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def hello_world():
    greeting = _("Hello world")
    title = _("Welcome to Holberton")
    username = g.user
    login = _("You are not logged in.")
    if username:
        login = _("You are logged in as {username}.").format(username=username)
    return render_template("6-index.html", greeting=greeting, title=title,
                           login=login)


def get_user(login_as):
    if login_as is None or login_as not in list(users.keys()):
        return None
    return users[login_as]


@app.before_request
def before_request():
    ids = None
    if request.args.get('login_as'):
        ids = int(request.args.get('login_as', None))
    user = get_user(ids)
    if user:
        g.user = user["name"]
    else:
        g.user = None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
