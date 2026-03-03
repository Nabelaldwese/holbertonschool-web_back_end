#!/usr/bin/env python3
"""Module that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a new document in the collection and return its _id"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
