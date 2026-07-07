from database import *

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Employee
    if choice == "1":

        name = input("Enter Employee Name: ")
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

    # View Employees
    elif choice == "2":

        cursor.execute("SELECT * FROM employees")

        rows = cursor.fetchall()

        print("\nEmployee Records:")

        for row in rows:
            print(row)

    # Search Employee
    elif choice == "3":

        emp_id = int(input("Enter Employee ID: "))

        query = "SELECT * FROM employees WHERE employee_id = %s"

        cursor.execute(query, (emp_id,))

        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found:")
            print(employee)
        else:
            print("Employee Not Found")

    # Update Employee
    elif choice == "4":

        emp_id = int(input("Enter Employee ID: "))
        new_department = input("Enter New Department: ")

        query = """
        UPDATE employees
        SET department = %s
        WHERE employee_id = %s
        """

        cursor.execute(query, (new_department, emp_id))
        conn.commit()

        print("Employee Updated Successfully")

    # Delete Employee
    elif choice == "5":

        emp_id = int(input("Enter Employee ID: "))

        query = "DELETE FROM employees WHERE employee_id = %s"

        cursor.execute(query, (emp_id,))
        conn.commit()

        print("Employee Deleted Successfully")

    # Exit
    elif choice == "6":

        print("Thank You!")
        break

    else:
        print("Invalid Choice")