import mysql.connector as myconn
import json
import sys

def connectsql(config):
    print(config)
    return 
    # if config['database']:
    #     conn = myconn.connect(
    #         user=config['user'], password=config['password'], database=config['database'])
    #     return conn


def getdatabase():
    base = getConfig()
    return base['database']

