#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    """Print the number of documents in this collection"""
    total_logs = nginx_collection.find().count()
    print("{} logs".format(total_logs))

    """Print the number of documents per method"""
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for m in method:
        num_logs = nginx_collection.find({"method": m}).count()
        print("\tmethod {}: {}".format(m, num_logs))

    """Print the number of documents with method=GET & path=/status"""
    num_doc = nginx_collection.find({"$and": [{"method": "GET"},
                                              {"path": "/status"}]}).count()
    print("{} status check".format(num_doc))
