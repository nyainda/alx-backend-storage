#!/usr/bin/env python3
""" Printing logs stats """
from pymongo import MongoClient


def logs_aggregate(collection):
    """
    Returns the logs stats
    """
    pipeline = [
        {'$group': {'_id': '$ip', 'count': {'$sum': 1}}},
        {'$sort': {'count': -1}},
        {'$limit': 10}
    ]
    return list(collection.aggregate(pipeline))


if __name__ == "__main__":
    """ Main function """
    collection = MongoClient('mongodb://localhost:27017').logs.nginx
    print(f'{collection.count_documents({})} logs')
    print('Methods:')
    print(f'\tmethod GET: {collection.count_documents({"method": "GET"})}')
    print(f'\tmethod POST: {collection.count_documents({"method": "POST"})}')
    print(f'\tmethod PUT: {collection.count_documents({"method": "PUT"})}')
    print(f'\tmethod PATCH: {collection.count_documents({"method": "PATCH"})}')
    print(
        f'\tmethod DELETE: {collection.count_documents({"method": "DELETE"})}')
    print(f'{collection.count_documents({"path": "/status"})} status check')

    print('IPs:')
    for log in logs_aggregate(collection):
        print(f'\t{log.get("_id")}: {log.get("count")}')
