-- SQL(Assignment)

CREATE DATABASE IF NOT EXISTS company;
USE company;

CREATE TABLE employee(
EmpID INT PRIMARY KEY,
FirstName VARCHAR(30),
LastName VARCHAR(30),
Department VARCHAR(50),
Salary INT,
HireDate DATE
);

INSERT INTO employee
(EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, "Alice", "Johnson", "IT", 6500, "2020-03-15"),
(102, "Mark", "Rivera", "HR", 4800, "2019-07-22"),
(103, "Sophia", "Lee", "Finance", 7200, "2021-01-10"),
(104, "Daniel", "Kim", "IT", 5800, "2018-11-05"),
(105, "Emma", "Brown", "Marketing", 5300, "2022-04-18"),
(106, "Liam", "Patel", "Finance", 6900, "2020-09-29"),
(107, "Olivia", "Garcia", "HR", 4600, "2017-06-30"),
(108, "Noah", "Thompson", "IT", 7500, "2023-02-12"),
(109, "Ava", "Martinez", "Marketing", 5100, "2019-02-12"),
(110, "Ethan", "Davis", "Finance", 8000, "2016-05-14");

-- AssignmentProblems

-- Q1. Write a query to display every employee and all their data
SELECT * FROM employee;

-- Q2. List only the FirstName, LastName, and Salary of every employee.
SELECT FirstName, LastName, Salary
FROM employee;

-- Q3. Show all employees who work in the 'IT' department.
SELECT *
FROM employee
WHERE Department = "IT";

-- Q4. Retrieve employees with a salary greater than 6000.
SELECT *
FROM employee
WHERE Salary > 6000;

-- Q5. List all employees ordered by HireDate from newest to oldest
SELECT *
FROM employee
ORDER BY HireDate DESC;

-- Q6. Show a list of all unique departments present in the table.
SELECT Department
FROM employee
GROUP BY Department;

SELECT DISTINCT Department
FROM employee;

-- Q7. Find employees whose first name starts with ‘A’.
SELECT *
FROM employee 
WHERE FirstName LIKE "A%";

-- Q8. Show employees whose salaries are between 4000 and 7000.
SELECT *
FROM employee 
WHERE Salary > 4000 and Salary < 7000;

SELECT *
FROM employee 
WHERE Salary BETWEEN 4000 AND 7000;

-- Q9. Find the average salary of all employees.
SELECT AVG(Salary)
FROM employee;

-- Q10. List each department along with the number of employees, but only include departments with more than 3 employees.
SELECT Department, COUNT(*)
FROM employee
GROUP BY Department
HAVING COUNT(*) >= 3;
