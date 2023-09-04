#!/usr/bin/env python3
""" 5.Mock logging in """
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


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


@babel.localeselector
def get_locale():
    """ Determine the best match with our supported languages """
    # Locale from URL parameters
    locale_arg = request.args.get('locale')
    if locale_arg:
        return locale_arg

    # Locale from user settings
    if g.user:
        locale = g.user["locale"]
        if locale in app.config['LANGUAGES']:
            return locale

    # Locale from request header
    locale = request.headers.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    # Default locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Find timezone parameter in URL parameters
    Find time zone from user settings
    Default to UTC
    """
    try:
        # Locale from URL parameters
        if request.args.get('timezone'):
            timezone = request.args.get('timezone')
            check_timezone = pytz.timezone(timezone)

        # Locale from user settings
        elif g.user and g.user["timezone"]:
            timezone = g.user["timezone"]
            check_timezone = pytz.timezone(timezone)

        # Default locale
        else:
            timezone = app.config['BABEL_DEFAULT_TIMEZONE']
            check_timezone = pytz.timezone(timezone)
    
    except pytz.exceptions.UnknownTimeZoneError:
        timezone = "UTC"

    return timezone



@app.route('/', methods=["GET"])
def index():
    """index page"""
    timezone = get_timezone()
    current_datetime = datetime.now(pytz.timezone(timezone))
    print(current_datetime)
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run()
