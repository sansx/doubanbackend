import mysql.connector as myconn
# import json
# import sys


# def getConfig():
#     with open('{path}\mysql.json'.format(path=sys.path[0]), 'r') as f:
#         data = json.load(f)
#     return data


def connectsql(config):
    if config['database']:
        conn = myconn.connect(
            user=config['user'], password=config['password'], database=config['database'])
        return conn


