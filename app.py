!pip install pymysql

import mysql.connector as connection

DATABASE_URL='data-case-db.ctxdyrkhld9x.us-east-1.rds.amazonaws.com'
DATABASE_NAME='warren'
DATABASE_USER='allana.cardoso'
DATABASE_PASSWORD='aX858M!am67sqxUl'

try:
    mydb = connection.connect(
        host = DATABASE_URL,
        database = DATABASE_NAME,
        user= DATABASE_USER,
        passwd = DATABASE_PASSWORD,use_pure=True
    )
    cursor = mydb.cursor()

    # query = "SELECT * FROM Customers;"

    # cursor.execute(query, multi=True)
    # print(cursor.fetchall())

    query = "SHOW TABLES;"
    # query = "SELECT CURDATE();"
    # Executing Query
    cursor.execute(query)

    # Above Query Gives Us The Current Date
    # Fetching Data
    m = cursor.fet()

    # Printing Result Of Above
    # print("Today's Date Is ", m[0])

    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
