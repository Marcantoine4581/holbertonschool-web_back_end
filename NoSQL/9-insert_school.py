#!/usr/bin/env python3
"""Insert a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
        kwargs: Key / Value arguments to be inserted
    Returns:
        The new _id
    """
    inserted_document = mongo_collection.insert_one(kwargs)
    return inserted_document.inserted_id
