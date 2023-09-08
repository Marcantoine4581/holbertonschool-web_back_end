#!/usr/bin/env python3
""" Module of session_auth views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv
from api.v1.app import auth


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
      - set a cookie to the response
      - 404 if no user found for this email
      - 400 if password missing
      - 401 if wrong password
    """
    email = request.form.get("email")
    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get("password")
    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        else:
            user_id = user.id
            from api.v1.app import auth
            session_id = auth.create_session(user_id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
    return jsonify({"error": "no user found for this email"}), 404


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /auth_session/logout
    Return:
        - empty JSON dictionary with the status code 200
        - If destroy_session returns False, abort(404)
    """
    from api.v1.app import auth

    deleted = auth.destroy_session(request)

    if not deleted:
        abort(404)

    return jsonify({}), 200
