import mysql.connector 

database = mysql.connector.connect(
    host = 'localhost',
    user = "root",
    passwd = "123456",
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE records")

print("ALL DONE")