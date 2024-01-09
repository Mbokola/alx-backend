#!/usr/bin/env python3
""" 0-app module
"""

from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """ Locale selector
    """
    user_preferred_language = request.args.get('locale', None)
    if user_preferred_language and user_preferred_language in Config.LANGUAGES:
        return user_preferred_language
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/")
def hello_world():
    greeting = _("Hello world")
    title = _("Welcome to Holberton")
    return render_template("4-index.html", greeting=greeting, title=title)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
