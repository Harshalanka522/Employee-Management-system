from database import *

cursor.execute("SELECT * FROM employees")

rows = cursor.fetchall()

print("Employee Records")

for row in rows:
    print(row)