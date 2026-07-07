from database import *

emp_id = int(input("Enter Employee ID: "))
new_dept = input("Enter New Department: ")

query = """
UPDATE employees
SET department = %s
WHERE employee_id = %s
"""

cursor.execute(query, (new_dept, emp_id))
conn.commit()

print("Employee Updated Successfully")