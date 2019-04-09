from connsql.connect import connectsql
from main import getsqlconfig
import pygal
import json

# print(getsqlconfig())
if __name__ == "__main__":
    conn = connectsql(getsqlconfig())
    cursor = conn.cursor()
    radar_chart = pygal.Radar()
    radar_chart.title = '豆瓣电影top5'
    radar_chart.x_labels = ["{}🌟".format(x) for x in range(1,6)]
    try:
        cursor.execute('select title,original_title,average,details  \
        from movies where hot=0 order by average desc limit 5')
        val = cursor.fetchall()
        for info in val:
            # print([(info[-1])[str(x+1)] for x in range(0,5) ])
            # print( json.loads(info[-1].replace("\'","\""))['1'])
            radar_chart.add(info[0], [json.loads(info[-1].replace("\'","\""))[str(x+1)] for x in range(0,5) ])
    except:
        conn.rollback()
        pass
    radar_chart.render_to_file('randar.svg')
    cursor.close()
    conn.close()
