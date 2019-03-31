import requests
import json
from connsql.connect import connectsql


def getsqlconfig():
    with open(r"mysql.json", "r") as f:
        res = json.load(f)
    return res


connectsql(getsqlconfig())


def getconfig():
    with open('config.json', "r") as f:
        res = json.load(f)
    return res

# conn = connect.connectsql()
# cursor = conn.cursor()
# cursor.execute("select * fro1m user")
# values = cursor.fetchall()


def getMovieInfo(count):
    res = getconfig()
    try:
        url = '{baseurl}/in_theaters?apikey={apikey}&city={city}&start={start}&count={count}&client=&udid='
        link = url.format(baseurl=res['baseUrl'],
                        apikey=res['apikey'], city="温州", start=0, count=count)
        r = requests.get(link)
        return r.json()
        pass
    except:
        pass

res = getMovieInfo(2)
if res:
    count = res["total"]
    with open("","") as target:
        pass
    print(count)
    pass
