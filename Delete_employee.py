from database import *

emp_id = int(input("Enter Employee ID: "))

query = "DELETE FROM employees WHERE employee_id = %s"

cursor.execute(query, (emp_id,))
conn.commit()

print("Employee Deleted Successfully")