#!/usr/bin/env python3
""" 5. Encrypting passwords """
import bcrypt


def hash_password(password: str) -> bytes:
    """ returns a salted, hashed password, which is a byte string """
    bytes = password.encode('utf-8')  # converting password to array of bytes
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt())  # Hashing the password
    return hashed
