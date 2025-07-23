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

    try:
         # establish the connection
        conn = createconnection()
        # create a cursor
        cursor =createCursor(conn)

        # Write a query
        #sql = "create table if not exists employees(empid int, name varchar(30), dept varchar(20))";
        sql = "insert into employees(empid,name,dept) values (%s,%s,%s)"
        empid = int(input("Enter empid "))
        name = input("Enter employee name ")
        dept = input("Enter employee department ")
        values = (empid, name, dept)
        #executet the query
        #cursor.execute(sql) # this is used to create the table
        cursor.execute(sql,values) # this is used to insert the values into table
        conn.commit()
        print("Data inserted.....!")
        #close the cursor or objects
        cursor.close()
        conn.close()
        #print("Table created Successfully")
    except mysql.connector.Error as err:
        print(err)