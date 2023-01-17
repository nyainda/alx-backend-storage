#!/usr/bin/env python3
""" Insert a new Data collection giving a dictionary of data """


def insert_school(mongo_collection, **kwargs):
    """ insert_school """
    return mongo_collection.insert_one(kwargs).inserted_id
