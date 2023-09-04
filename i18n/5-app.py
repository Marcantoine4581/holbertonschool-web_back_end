#!/usr/bin/env python3
""" 5.Mock logging in """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    locale_arg = request.args.get('locale')
    if locale_arg:
        return locale_arg
    return request.accept_languages.best_match(app.config['LANGUAGES'])


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ function that returns a user dictionary or None if the ID cannot be
    found or if login_as was not passed"""
    try:
        user_id = request.args.get('login_as')
        user = users[int(user_id)]
    except Exception:
        user = None
    return user


@app.before_request
def before_request():
    """Before request executed before all other functions"""
    g.user = get_user()


@app.route('/', methods=["GET"])
def index():
    """index page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
