#!/usr/bin/env python3
"""List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """function that lists all documents in a collection
    Args:
        mongo_collection (): a mongo collection
    Returns:
        All documents in a collection
        OR an empty list if no document in the collection
    """
    if mongo_collection.count() == 0:
        return []
    return mongo_collection.find()
