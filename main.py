import requests
import json
from connsql.connect import connectsql


def getsqlconfig():
    with open(r"mysql.json", "r") as f:
        res = json.load(f)
    return res


# connectsql(getsqlconfig())


def getconfig():
    with open('config.json', "r") as f:
        res = json.load(f)
    return res


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
conn = connectsql(getsqlconfig())
cursor = conn.cursor()
# print(res)
if res:
    count = res["total"]
    try:
        re = getMovieInfo(count)
        # print(json.dumps(re["subjects"], ensure_ascii=False, indent=2))
        # cursor.execute('select * from movies')
        # values = cursor.fetchall()
        # print(values) 
        with open("moviedata.json", "wt") as f:
            f.write("aaa")
            pass
        for info in re["subjects"]:
            print(info["title"], info["original_title"],
                  info["durations"], info["id"])
            print("insert into movies (movie_id,original_title,title,durations) values ({}, '{}','{}','{}') where movie_id={} not in (select movie_id from movies)".format(info["id"], info["original_title"], info["title"], json.dumps(info["durations"]), info["id"]))
            cursor.execute(
                "insert into movies (movie_id,original_title,title,durations) values (%s, %s,%s,%s) where %s not in (select movie_id from movies)",
                [info["id"], info["original_title"], info["title"], json.dumps(info["durations"]), info["id"]])
            conn.commit()
        cursor.close()
        conn.close()
    except:
        pass
    # getMovieInfo(count)
