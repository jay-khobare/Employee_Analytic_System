from config.connection import get_db_connection
from services.analytic_service import department_employee_count,highest_paid_employee,department_average_salary,employee_summary_report
from services.employee_service import (get_all_employees_data, 
                                       get_employee_data, 
                                       add_employee_data, 
                                       update_employee_data,
                                       delete_employee_data)

def view_employees():
    print("===================================")
    print("         Employees Details         ")
    print("===================================")
    employees=get_all_employees_data()
    for employee in employees:
        print(f"{employee[0]:<5}{employee[1]:<20}{employee[2]:<12}{employee[3]:<12}{employee[4]:<5}")
    print("===================================")
    

def search_employee():
    print("==========================")
    employee_id=int(input("Enter the Employee ID: "))
    result = get_employee_data(employee_id)
    
    if result:
        employee={
            "employee_id":result[0],
            "employee_name":result[1],
            "department_name":result[2],
            "employee_salary":result[3],
            "department_id":result[4]
        }
        print("==========================")
        print("Employee Details:")
        print("==========================")
        print(f"Employee ID     : {employee['employee_id']:<20}")
        print(f"Department ID   : {employee['department_id']:<20}")
        print(f"Employee Name   : {employee['employee_name']:<20}")
        print(f"Department Name : {employee['department_name']:<20}")
        print(f"Employee Salary : {employee['employee_salary']:<20}")
        print("==========================")
    else:
        print("No Employee Found.")


def add_employee():
    e_id=int(input("Enter New Employee ID: "))
    e_name=str(input("Enter New Employee Name: "))
    e_dept=str(input("Enter New Employee Department: "))
    e_salary=int(input("Enter New Employee Salary: "))
    e_dept_id=int(input("Enter New Employee Department ID: "))
    existing_employee=get_employee_data(e_id)
    if existing_employee:
        print("=================================")
        print("   Employee ID Already Exists    ")
        print("=================================")
        return
    
    result=add_employee_data(e_id,e_name,e_dept,e_salary,e_dept_id)
    if result:
        print("=================================")
        print("   Employee Added Successfully   ")
        print("=================================")
    else:
        print("=================================")
        print("    Department ID Not Found.     ")
        print("=================================")


def update_employee():
    print("======================")
    print("    Update Employee   ")
    print("======================")
    em_id=int(input("Enter Employee ID to Update: "))
    em_name=str(input("Enter New Employee Name: "))
    em_dept=str(input("Enter New Employee Department: "))
    em_salary=int(input("Enter New Employee Salary: "))
    em_dept_id=int(input("Enter New Employee Department ID: "))
    result=update_employee_data(em_id,em_name,em_dept,em_salary,em_dept_id)
    if result == "employee_not_found":
        print("=================================")
        print("        Employee Not Found       ")
        print("=================================")

    elif result == "department_not_found":
        print("=================================")
        print("       Department Not Found      ")
        print("=================================")

    elif result == 1:
        print("=================================")
        print("       Update Successfully       ")
        print("=================================")


def remove_employee():
    print("===================================")
    print("           Remove Employee         ")
    print("===================================")
    em_id=int(input("Enter Employee ID to Remove: "))
    result=delete_employee_data(em_id)
    if result=="employee_not_found":
        print("===================================")
        print("        Employee Not Found.        ")
        print("===================================")
    elif result:
        print("==========================================")
        print("       Employee Deleted Successfully.     ")
        print("==========================================")
    

while True:
    print("=================================")
    print("   Employee Management System   ")
    print("=================================")

    print("1. View All Employee")
    print("2. Search Employee")
    print("3. Add Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Employee Analytics")
    print("7. Exit")
    print("=================================")
    try:
        choice=(int(input("Enter Your Choice: ")))
    except ValueError:
        print("Please Enter a Valid Choice.")
        continue
    print("=================================")
    if choice==1:view_employees()
    elif choice==2:search_employee()
    elif choice==3:add_employee()
    elif choice==4:update_employee()
    elif choice==5:remove_employee()
    elif choice==6:
        while True:
            print("=================================")
            print("        Employee Analytics       ")
            print("=================================")
            
            print("1. Total Employee in Company")
            print("2. Average Salary")
            print("3. Highest Paid Employee")
            print("4. Employee Summary")
            print("5. Exit")
            print("=================================")
            try:
                analytic_choice=(int(input("Enter Your Choice: ")))
            except ValueError:
                print("Please Enter A Valid Choice.")
                continue
            if analytic_choice==1:
                result=department_employee_count()
                print(result)
            elif analytic_choice==2:
                result=department_average_salary()
                print(result)
            elif analytic_choice==3:
                result=highest_paid_employee()
                print(result)
            elif analytic_choice==4:
                employee_summary_report()
            elif analytic_choice==5:
                print("Exiting........")
                break
            else:print("Invalid Choice")
    elif choice==7:
        print("Exiting.......")
        break
    else:print("Invalid Choice.")