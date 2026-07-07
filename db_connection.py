import mysql.connector

print("Before connect")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsha"
)

print("After connect")

cursor = conn.cursor()

print("Before select")

cursor.execute("SELECT 1")

print("After select")

print(cursor.fetchone())
