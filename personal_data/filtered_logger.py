#!/usr/bin/env python3
""" 0. Regex-ing """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Replace occurrences of certain field values.
    Args:
        fields (List[str]): Representing all fields to obfuscate.
        redaction (str): Representing by what the field will be obfuscated
        message (str): Representing the log line.
        separator (str): Representing by which character is separating all
            fields in the log line (message).
    Returns:
        The log message obfuscated.
    """
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
