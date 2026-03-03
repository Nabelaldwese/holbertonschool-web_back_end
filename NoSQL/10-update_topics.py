#!/usr/bin/env python3
"""Module that updates school topics based on name"""


def update_topics(mongo_collection, name, topics):
    """Update topics of all documents with a given name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
