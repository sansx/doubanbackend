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


def getMovielist(count, type="hot"):
    urlDir = {"hot": '{baseurl}/in_theaters?apikey={apikey}&city={city}&start={start}&count={count}&client=&udid=',
              "top": '{baseurl}/top250?apikey={apikey}&city={city}&start={start}&count={count}&client=&udid='}
    res = getconfig()
    try:
        url = urlDir[type]
        link = url.format(baseurl=res['baseUrl'],
                          apikey=res['apikey'], city="温州", start=0, count=count)
        r = requests.get(link)
        return r.json()
    except:
        pass


def getAll(type="hot"):
    res = getMovielist(1, type=type)
    if res:
        count = res["total"]
        print("获取热映电影成功[{}]".format(count))
        try:
            re = getMovielist(count, type=type)
            return re
        except:
            pass


def inputJson(*, fileName, info):
    with open("moviedata.json", "wt") as f:
        f.write(json.dumps(info, ensure_ascii=False, indent=2))
        pass


if __name__ == "__main__":
    conn = connectsql(getsqlconfig())
    cursor = conn.cursor()
    re = getAll()
    # print(re)
    cursor.execute("update movies set hot=false")
    for info in re["subjects"]:
        print(info["title"], info["original_title"],
                info["durations"], info["id"])
        # print(json.dumps(re["subjects"], ensure_ascii=False, indent=2))
        # cursor.execute('select * from movies')
        # values = cursor.fetchall()
        # print(values)
        # print("insert into movies (movie_id,original_title,title,durations) values ({}, '{}','{}','{}')".format(
        #     info["id"], info["original_title"], info["title"], json.dumps(info["durations"]), info["id"]))
        try:
            cursor.execute(
                "insert into movies (movie_id,original_title,title,durations,hot) \
                values (%s, '%s','%s','%s',true) \
                ON DUPLICATE KEY UPDATE hot=true" %
                (info["id"], info["original_title"], info["title"], json.dumps(info["durations"])))
            conn.commit()
        except:
            conn.rollback()
    res = getAll(type="top")
    print("添加top250电影中。。。")
    for info in res["subjects"]:
        # print(info["title"], info["original_title"],
        #         info["durations"], info["id"])
        # print(json.dumps(re["subjects"], ensure_ascii=False, indent=2))
        # cursor.execute('select * from movies')
        # values = cursor.fetchall()
        # print(values)
        # print("insert into movies (movie_id,original_title,title,durations) values ({}, '{}','{}','{}')".format(
        #     info["id"], info["original_title"], info["title"], json.dumps(info["durations"]), info["id"]))
        try:
            cursor.execute(
                "insert into movies (movie_id,original_title,title,durations) \
                values (%s, '%s','%s','%s')" %
                (info["id"], info["original_title"], info["title"], json.dumps(info["durations"])))
            conn.commit()
        except:
            conn.rollback()
    cursor.close()
    conn.close()

    # getMovielist(count)
