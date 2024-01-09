#!/usr/bin/env python3
""" 0-app module
"""

from flask import Flask, render_template
from flask_babel import Babel

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


@app.route("/")
def hello_world():
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
