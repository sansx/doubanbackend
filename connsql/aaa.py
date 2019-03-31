import connect

conn = connect.connectsql()
cursor = conn.cursor()
cursor.execute("select * from user")
values = cursor.fetchall()

def fetch(val):
    for x in val:
        pass



print(values)





