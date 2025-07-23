import mysql.connector

def createconnection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password@1",
        database="training"
    )
    return conn

def createCursor(conn):
    cursor = conn.cursor()
    return cursor

if __name__ == '__main__':
    conn = createconnection()
    cursor = createCursor(conn)
    sql = "select * from employees"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(type(data))
    for row in data:
        print(row)
        print(type(row))

