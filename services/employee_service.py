from database.employee_repository import get_all_employees, get_employee_by_id, add_employee, get_department_by_id, update_employee

def get_all_employees_data():
    employees=get_all_employees()
    return employees

def get_employee_data(employee_id):
    employee=get_employee_by_id(employee_id)
    return employee

def add_employee_data(employee_id,employee_name,employee_department,employee_salary,department_id):
    department=get_department_data(department_id)
    if not department:
        return None
    employee_add=add_employee(employee_id,employee_name,employee_department,employee_salary,department_id)
    return employee_add

def get_department_data(department_id):
    department=get_department_by_id(department_id)
    return department

def update_employee_data(employee_id,employee_name,employee_department,employee_salary,department_id):
    employee=get_employee_data(employee_id)
    
    if not employee:
        return "employee_not_found"
    
    department=get_department_data(department_id)
    
    if not department:
        return "department_not_found"
    
    update_rows=update_employee(employee_id,employee_name,employee_department,employee_salary,department_id)
    return update_rows

