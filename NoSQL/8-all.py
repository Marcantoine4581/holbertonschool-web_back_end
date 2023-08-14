#!/usr/bin/env python3
"""List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    if mongo_collection.count() == 0:
        return []
    return mongo_collection.find()
