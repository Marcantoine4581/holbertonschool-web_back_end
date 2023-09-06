#!/usr/bin/env python3
""" 0. Regex-ing """
from typing import List
import re
import logging
import mysql.connector
import os


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """ returns logging.Logger object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ returns a connector to the database
    (mysql.connector.connection.MySQLConnection object) """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db = os.environ.get("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(host=host,
                                         database=db,
                                         user=username,
                                         password=password)
    return connection


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filtering values in incoming log records using filter_datum """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def main():
    """ will obtain a database connection using get_db and retrieve all rows
    in the users table and display each row under a filtered format """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = cursor.column_names
    print(fields)

    logger = get_logger()

    for row in cursor:
        new_row = "".join(f'{field}={value}; '
                          for field, value in zip(fields, row))
        logger.info(new_row.strip())
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
