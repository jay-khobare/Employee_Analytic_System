use employee_analytics;

select count(employee_id) as total_employees from employees;

select avg(employee_salary) as average_salary from employees;

select sum(employee_salary) as total_salary from employees;

select min(employee_salary) as lowest_salary from employees;

select max(employee_salary) as highest_salary from employees;

select avg(employee_salary) as average_salary
from employees
group by
    employee_department;

select
    employee_department,
    avg(employee_salary) as average_salary
from employees
group by
    employee_department;

select
    employee_department,
    count(employee_id) as total_employees
from employees
group by
    employee_department;

select
    employee_department,
    count(employee_id) as total_employees,
    avg(employee_salary) as average_salary
from employees
group by
    employee_department;

select
    employee_department,
    count(employee_id) as total_employees,
    avg(employee_salary) as average_salary
from employees
group by
    employee_department
order by average_salary desc;

select
    employee_department,
    count(employee_id) as total_employees,
    avg(employee_salary) as average_salary
from employees
group by
    employee_department
order by average_salary asc;

select
    employee_department,
    count(employee_id) as total_employees,
    avg(employee_salary) as average_salary
from employees
group by
    employee_department
having
    average_salary > 45000;

select
    employee_department,
    count(employee_id) as total_employees,
    avg(employee_salary) as average_salary
from employees
group by
    employee_department
having
    total_employees >= 2
order by employee_department desc;

select
    employee_name,
    department_name,
    manager_name,
    employee_salary
from employees
    join departments on employees.department_id = departments.department_id
where
    department_name = 'IT';

select
    employee_name,
    department_name,
    manager_name,
    employee_salary
from employees
    join departments on employees.department_id = departments.department_id
where
    department_name = 'IT'
    AND employee_salary BETWEEN 40000 and 50000;

select
    employee_name,
    department_name,
    manager_name,
    employee_salary
from employees
    join departments on employees.department_id = departments.department_id
where
    employee_salary BETWEEN 40000 and 50000;

select
    employee_name,
    department_name,
    manager_name,
    employee_salary
from employees
    join departments on employees.department_id = departments.department_id
where (
        department_name = 'IT'
        and employee_salary > 45000
    )
    or (
        department_name = 'HR'
        and employee_salary > 40000
    );

SELECT
    employee_name,
    department_name,
    manager_name,
    employee_salary
from employees
    join departments on employees.department_id = departments.department_id
WHERE
    department_name IN ('IT', 'HR');

SELECT
    employee_name,
    department_name,
    manager_name,
    employee_salary
from employees
    join departments on employees.department_id = departments.department_id
WHERE
    department_name NOT IN('IT', 'HR');

SELECT
    department_name,
    AVG(employee_salary) AS department_average_salary
from employees
    JOIN departments ON employees.department_id = departments.department_id
GROUP BY
    department_name
HAVING
    department_average_salary > 45000;

select
    count(employee_id) as total_employees,
    department_name,
    AVG(employee_salary) AS average_salary
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
GROUP BY
    department_name
HAVING
    total_employees >= 2;

SELECT
    department_name,
    COUNT(employee_id) AS total_employees,
    AVG(employee_salary) AS average_salary
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
GROUP BY
    department_name
HAVING
    total_employees >= 2
    AND average_salary > 40000;

SELECT
    department_name,
    COUNT(employee_id) AS total_employees,
    AVG(employee_salary) AS average_salary
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
GROUP BY
    department_name
HAVING
    total_employees >= 1
ORDER BY average_salary DESC;

SELECT
    department_name,
    employee_id,
    employee_name,
    employee_salary
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
WHERE
    employee_salary = (
        SELECT MAX(e2.employee_salary) AS highest_salary
        FROM employees e2
        WHERE
            e2.department_id = employees.department_id
    );

SELECT
    department_name,
    employee_id,
    employee_name,
    employee_salary
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
WHERE (
        SELECT COUNT(*)
        FROM employees e2
        WHERE
            e2.department_id = employees.department_id
            AND e2.employee_salary > employees.employee_salary
    ) = 1;

SELECT * FROM employees;

UPDATE employees SET department_id = 1 WHERE employee_id = 6;

UPDATE employees
SET
    employee_name = "Gautam Chouhan"
WHERE
    employee_id = 2;

UPDATE employees
SET
    employee_name = "Vikram Rathore"
WHERE
    employee_id = 4;

UPDATE employees
SET
    employee_name = "Neha Tripathi"
WHERE
    employee_id = 3;

UPDATE employees
SET
    employee_name = "Ajay Singh"
WHERE
    employee_id = 5;

UPDATE employees
SET
    employee_name = "Rohit Sharma"
WHERE
    employee_id = 6;

SELECT
    department_name,
    employee_id,
    employee_name,
    employee_salary
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
WHERE (
        SELECT COUNT(*)
        FROM employees e2
        WHERE
            e2.department_id = employees.department_id
            AND e2.employee_salary > employees.employee_salary
    ) = 0;