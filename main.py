import json
from connsql.connect import connectsql

def getsqlconfig():
    with open(r"mysql.json","r") as f:
        res = json.load(f)
    return res

connectsql(getsqlconfig())