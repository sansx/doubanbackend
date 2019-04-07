import requests
import json
import sys
from ..connsql import connect

def getconfig():
    with open('{path}\config.json'.format(path=sys.path[0])) as f:
        res = json.load(f)
    return res

# conn = connect.connectsql()
# cursor = conn.cursor()
# cursor.execute("select * from user")
# values = cursor.fetchall()

res=getconfig()
url = '{baseurl}/in_theaters?apikey={apikey}&city={city}&start={start}&count={count}&client=&udid='
link = url.format(baseurl=res['baseUrl'],apikey=res['apikey'],city="温州",start=0,count=2)
r = requests.get(link)
print(r.json())




