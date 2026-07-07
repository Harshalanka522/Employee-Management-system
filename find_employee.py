from database import *

emp_id = int(input("Enter Employee ID: "))

query = "SELECT * FROM employees WHERE employee_id = %s"

cursor.execute(query, (emp_id,))

employee = cursor.fetchone()

if employee:
    print("\nEmployee Found:")
    print(employee)
else:
    print("Employee Not Found")