#!/usr/bin/env python3
""" Class basic auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ Class basic Auth """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Class basic Auth
        Returns the Base64 part of the Authorization header
        for a Basic Authentication: """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """ Returns the decoded value of a Base64 string
        base64_authorization_header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if decoded_base64_authorization_header.find(":") == -1:
            return None, None

        list_email_pwd = decoded_base64_authorization_header.split(":")
        return list_email_pwd[0], list_email_pwd[1]

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Returns the User instance based on his email and password """
        if not user_email or not isinstance(user_email, str):
            return None
        if not user_pwd or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """  overloads Auth and retrieves the User instance for a request """
        auth_header = self.authorization_header(request)

        if not auth_header:
            return None

        encoded = self.extract_base64_authorization_header(auth_header)
        if not encoded:
            return None

        decoded = self.decode_base64_authorization_header(encoded)
        if not decoded:
            return None

        email, pwd = self.extract_user_credentials(decoded)
        if not email or not pwd:
            return None

        user = self.user_object_from_credentials(email, pwd)
        return user
