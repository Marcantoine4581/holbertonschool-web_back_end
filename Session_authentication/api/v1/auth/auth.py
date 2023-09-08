#!/usr/bin/env python3
""" Class auth
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth():
    """ Class Auth """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if a path requires an authentication
        Returns:
            True if path is None
            True if excluded_paths is None or empty
            False if path is in excluded_paths
        """
        if path is None:
            return True
        if excluded_paths == [] or excluded_paths is None:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ Authorization_header """
        if request:
            return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current_user """
        return None

    def session_cookie(self, request=None):
        """ returns a cookie value from a request """
        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")
        if SESSION_NAME is None:
            return None

        _my_session_id = request.cookies.get(SESSION_NAME)
        return _my_session_id
