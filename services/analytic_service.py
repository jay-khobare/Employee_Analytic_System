from config.connection import get_db_connection

def department_employee_count():
    print("===================================")
    print("        Total Employee Count       ")
    print("===================================")

    connection=get_db_connection()
    cursor=connection.cursor()

    cursor.execute("SELECT employee_department, count(employee_id)AS total_employees from employees group by employee_department")
    employees=cursor.fetchall()
    # for employee in employees:
    #     print(f"{employee[0]:<12}{employee[1]:<12}")
    cursor.close()
    connection.close()
    return employees
def department_average_salary():    
    print("===================================")
    print("     Average Department Salary     ")
    print("===================================")

    connection=get_db_connection()
    cursor=connection.cursor()

    cursor.execute("Select employee_department, avg(employee_salary) as average_salary from employees group by employee_department order by average_salary")
    employees=cursor.fetchall()
    # for employee in employees:
    #     print(f"{employee[0]:>12}{employee[1]:>12,.2f}")
    cursor.close()
    connection.close()
    return employees

def highest_paid_employee():
    print("===================================")
    print("       Highest Paid Employee       ")
    print("===================================")

    connection=get_db_connection()
    cursor=connection.cursor()

    cursor.execute("select employee_id, employee_name, employee_department, employee_salary from employees order by employee_salary desc limit 1")
    employees=cursor.fetchall()
    # for employee in employees:
    #     print(f"{employee[0]:>12}{employee[1]:>15}{employee[2]:>15}{employee[3]:>12,.2f}")
    cursor.close()
    connection.close()
    return employees

def employee_summary_report():
    department_counts=department_employee_count()
    highest_paid=highest_paid_employee()
    company_salary=company_average_salary()
    highest_paid_data=highest_paid[0]
    total_department_counts=0

    for employee in department_counts:
        total_department_counts+=employee[1]
    print("===================================")
    print("          Employee Summary         ")
    print("===================================")
    print(f"Total Employees: {total_department_counts}")
    print(f"Average Company Salary: ₹{company_salary[0][0]:,.2f}")
    print(f"Highest Paid Employee: {highest_paid_data[1]}")
    print(f"Highest Salary: {highest_paid_data[3]:,.2f}")
    print("===================================")
    print("        Department Breakdown       ")
    print("===================================")
    for employee in department_counts:
        print(f"{employee[0]:>15}{employee[1]:>15}")


def company_average_salary():
    connection=get_db_connection()
    cursor=connection.cursor()
    cursor.execute("select avg(employee_salary)as company_average_salary from employees")
    salary=cursor.fetchall()
    cursor.close()
    connection.close()
    return salary