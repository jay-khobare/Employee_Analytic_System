create table employees(
employee_id int primary key,
employee_name varchar(50),
employee_department varchar(50),
employee_salary int
);

alter table employees
add column department_id int;