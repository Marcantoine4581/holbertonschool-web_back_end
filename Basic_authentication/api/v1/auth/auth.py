#!/usr/bin/env python3
""" Class auth
"""
from flask import request
from typing import List, TypeVar


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if a path requires an authentication """
        return False

    def authorization_header(self, request=None) -> str:
        """ Authorization_header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Current_user """
        return None
