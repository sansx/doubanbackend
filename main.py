import requests
import json
from math import ceil
from time import sleep
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


def getMovielist(count, start=0, type="hot"):
    urlDir = {"hot": '{baseurl}/in_theaters?apikey={apikey}&city={city}&start={start}&count={count}&client=&udid=',
              "top": '{baseurl}/top250?apikey={apikey}&start={start}&count={count}&client=&udid='}
    res = getconfig()
    try:
        url = urlDir[type]
        link = url.format(baseurl=res['baseUrl'],
                          apikey=res['apikey'], city="温州", start=start, count=count)
        r = requests.get(link)
        return r.json()
    except:
        pass


def getAll(type="hot", limit=50):
    res = getMovielist(1, type=type)
    if res:
        count = res["total"]
        print("获取热映电影成功[{}]".format(count))
        if count > limit:
            arr = []
            page = ceil(count/limit)
            for i in range(page):
                re = getMovielist(limit, start=i*limit, type=type)
                print("start:{},count:{},num:{}".format(
                    re["start"], re["count"], len(re["subjects"])))
                arr.append(re)
                sleep(5)
                pass
            return arr
        try:
            re = getMovielist(count, type=type)
            return re
        except:
            pass


def inputJson(*, fileName="moviedata.json", info):
    with open(fileName, "at+", encoding="utf-8") as f:
        f.write(json.dumps(info, ensure_ascii=False, indent=2))
        pass


if __name__ == "__main__":
    conn = connectsql(getsqlconfig())
    cursor = conn.cursor()
    re = getAll()
    # print(re)
    cursor.execute("truncate movies")
    for info in re["subjects"]:
        # print(json.dumps(re["subjects"], ensure_ascii=False, indent=2))
        # cursor.execute('select * from movies')
        # values = cursor.fetchall()
        # print(values)
        # print("insert into movies (movie_id,original_title,title,durations,average,details) values ({}, '{}','{}','{}',{},{})".format(
        #     info["id"], info["original_title"], info["title"], json.dumps(info["durations"]),
        #     info["rating"]["average"], json.dumps(info["rating"]["details"]).replace("\'", "\\'")))
        try:
            cursor.execute(
                "insert into movies (movie_id,original_title,title,durations,hot,average,details) \
                values (%s, '%s', '%s', '%s', true, %s, '%s' ) \
                ON DUPLICATE KEY UPDATE hot=true" %
                (info["id"], info["original_title"], info["title"],
                 json.dumps(info["durations"]), info["rating"]["average"], str(info["rating"]["details"]).replace("\'", "\\'")))
            conn.commit()
        except:
            conn.rollback()
    res = getAll(type="top", limit=100)

    print("添加top250电影中。。。")
    if type(res) == list:
        for i in res:
            for info in i["subjects"]:
                for key in info:
                    if type(info[key]) == str and "'" in info[key]:
                        info[key] = info[key].replace("'", "\\'")
                    if key == "durations" and info[key] is None:
                        print(info["title"])
                    # print("insert into movies (movie_id,original_title,title,durations) values ({}, '{}','{}','{}')".format(
                    # info["id"], info["original_title"], info["title"], json.dumps(info["durations"]), info["id"]))
                try:
                    cursor.execute("insert into movies (movie_id,original_title,title,durations,average,details) \
                        values (%s, '%s','%s','%s', %s, '%s')" %
                        (info["id"], info["original_title"], info["title"], json.dumps(info["durations"]),
                        info["rating"]["average"], str(info["rating"]["details"]).replace("\'", "\\'")))
                    conn.commit()
                except:
                    # inputJson(info=",{}".format(info))
                    conn.rollback()
    cursor.close()
    conn.close()
