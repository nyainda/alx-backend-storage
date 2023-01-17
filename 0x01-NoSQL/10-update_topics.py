#!/usr/bin/env python3
""" Update many documents """


def update_topics(mongo_collection, name, topics):
    """ update_topics """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}})
