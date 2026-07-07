import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="harsha",
    database="employe_db"
)

cursor = conn.cursor()

print("Connected Successfully")