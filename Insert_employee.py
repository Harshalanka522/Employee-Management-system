from database import *

name = input("Enter Name: ")
department = input("Enter Department: ")
email = input("Enter Email: ")
phone = input("Enter Phone: ")
joining_date = input("Enter Joining Date (YYYY-MM-DD): ")

query = """
INSERT INTO employees
(employee_name, department, email, phone, joining_date)
VALUES (%s, %s, %s, %s, %s)
"""

values = (name, department, email, phone, joining_date)

cursor.execute(query, values)
conn.commit()

print("Employee Added Successfully")