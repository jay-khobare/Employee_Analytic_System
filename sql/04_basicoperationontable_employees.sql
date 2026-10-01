use employee_analytics;
select*from employees;
select * from employees where employee_department="IT";
select*from employees where employee_salary >45000;
select*from employees where employee_department="IT" and employee_salary >40000;
select*from employees where employee_salary between 40000 and 50000;

select department_id from employees;