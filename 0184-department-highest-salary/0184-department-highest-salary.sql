# Write your MySQL query statement below
WITH MaxSalary AS (
    SELECT D.id as departmentId, MAX(E.salary) as Salary
    FROM Employee E INNER JOIN Department D ON E.departmentId = D.id
    GROUP BY D.id
)
SELECT D.name as Department, E.name as Employee, E.salary as Salary
FROM Employee E
    INNER JOIN Department D ON E.departmentId = D.id
    INNER JOIN MaxSalary MS ON MS.departmentId = D.id
WHERE MS.Salary = E.Salary