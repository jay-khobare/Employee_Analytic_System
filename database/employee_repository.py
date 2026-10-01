from config.connection import get_db_connection

# View All Employees Function
def get_all_employees():

    connection=get_db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM employees")

    employees=cursor.fetchall()

    cursor.close()
    connection.close()

    return employees

# Employee Searching Function
def get_employee_by_id(employee_id):
    
    connection=get_db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM employees WHERE employee_id=%s",(employee_id,))

    employee=cursor.fetchone()

    cursor.close()
    connection.close()

    return employee

# Add Employee Function
def add_employee(employee_id, employee_name, employee_department, employee_salary, department_id):
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""INSERT INTO Employees
                       (employee_id,
                        employee_name,
                        employee_department,
                        employee_salary,
                        department_id)
                        VALUES(%s,%s,%s,%s,%s)""",
                        (employee_id,employee_name,employee_department,employee_salary,department_id))
    row_affected=cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()
    return row_affected

# Department Validation Function
def get_department_by_id(department_id):
    connection=get_db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM departments WHERE department_id=%s",(department_id,))
    department=cursor.fetchone()

    cursor.close()
    connection.close()
    return department

# Update Employee Function
def update_employee(employee_id,employee_name,employee_department,employee_salary,department_id):
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""UPDATE employees 
                   SET employee_name=%s,
                   employee_department=%s,
                   employee_salary=%s,
                   department_id=%s
                   WHERE employee_id = %s""",
                   (employee_name,employee_department,employee_salary,department_id,employee_id))
    connection.commit()
    updated_employee=cursor.rowcount
    cursor.close()
    connection.close()
    return updated_employee

def delete_employee(employee_id):
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("""DELETE FROM employees
                   WHERE employee_id=%s""", 
                   (employee_id,))
    connection.commit()
    deleted_rows =cursor.rowcount
    cursor.close()
    connection.close()
    return deleted_rows

