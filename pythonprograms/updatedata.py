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
    #sql = "update employees set dept = %s, name = %s where empid = %s"
    sql = "delete from employees where empid = %s"
    empid = int(input("Enter empid"))
    #name = input("Enter name")
    #dept = input("Enter dept")
    #cursor.execute(sql, (dept,name,empid)) # this is for update
    cursor.execute(sql,(empid,))
    conn.commit()
    #print("Data updated successfully..!")
    print("Data deleted ...!")
    cursor.close()
    conn.close()

