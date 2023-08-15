#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """function that changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name (str): the school name to update.
        topics (list of strings): list of topics approached in the school
    Returns:
        The document updated
		None if no document updated
    """
    return mongo_collection.update_many(
        {"name": name},
        {
            "$set": {"topic": topics}
        }
    )
