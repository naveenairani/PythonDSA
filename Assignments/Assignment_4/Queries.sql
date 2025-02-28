- 1. Select employee details of dept number 10 or 30
SELECT *
FROM Emp
WHERE DeptNo IN (10, 30);

- 2. Fetch all the dept details with more than 1 Employee
SELECT d.DeptNo, d.Dname, d.Loc
FROM Dept d
JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.DeptNo, d.Dname, d.Loc
HAVING COUNT(*) > 1;

- 3. Fetch employee details whose name starts with the letter “S”
SELECT *
FROM Emp
WHERE Ename LIKE 'S%';

- 4. Select Emp Details whose experience is more than 2 years
SELECT *
FROM Emp
WHERE TIMESTAMPDIFF(YEAR, Hire_Date, CURDATE()) > 2;

- 5. Replace the char “a” with “#” in Employee Name
SELECT EmpNo, REPLACE(Ename, 'a', '#') AS ModifiedName
FROM Emp;

- 6. Fetch employee name and his/her manager name
SELECT e.Ename AS Employee, m.Ename AS Manager
FROM Emp e
LEFT JOIN Emp m ON e.Mgr = m.EmpNo;

- 7. Fetch Dept Name and Total Salary of the Dept
SELECT d.Dname, SUM(e.Sal) AS TotalSalary
FROM Dept d
JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.Dname;

- 8. Fetch ALL employee details along with department name and location (even if a department has no employees)
SELECT e.*, d.Dname, d.Loc
FROM Dept d
LEFT JOIN Emp e ON d.DeptNo = e.DeptNo;

- 9. Increase the employee salary by 10%
UPDATE Emp
SET Sal = Sal * 1.10;

- 10. Delete employees belonging to the department located in Chennai
DELETE FROM Emp
WHERE DeptNo IN (SELECT DeptNo FROM Dept WHERE Loc = 'Chennai');

- 11. Get Employee Name and Gross Salary (Sal + Commission)
SELECT Ename, Sal + COALESCE(Commission, 0) AS GrossSalary
FROM Emp;

- 12. Increase the data length of the column Ename of Emp table from 100 to 250
ALTER TABLE Emp
MODIFY Ename VARCHAR(250);

- 13. Get the current datetime
SELECT NOW() AS CurrentDateTime;

- 14. Create a STUDENT table with 5 related columns
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    Course VARCHAR(50),
    Year INT,
    Department VARCHAR(50)
);

- 15. Fetch the number of employees who are getting salary more than 10000
SELECT COUNT(*) AS NumEmployees
FROM Emp
WHERE Sal > 10000;

- 16. Fetch minimum salary, maximum salary and average salary from Emp table
SELECT MIN(Sal) AS MinSalary,
       MAX(Sal) AS MaxSalary,
       AVG(Sal) AS AvgSalary
FROM Emp;

- 17. Fetch the number of employees in each location
SELECT d.Loc, COUNT(*) AS NumEmployees
FROM Dept d
JOIN Emp e ON d.DeptNo = e.DeptNo
GROUP BY d.Loc;

- 18. Display employee names in descending order
SELECT Ename
FROM Emp
ORDER BY Ename DESC;

- 19. Create a new table (EMP_BKP) from the existing EMP table
CREATE TABLE EMP_BKP AS
SELECT * FROM Emp;

- 20. Fetch first 3 characters from employee name appended with salary
SELECT CONCAT(LEFT(Ename, 3), Sal) AS NameWithSalary
FROM Emp;

- 21. Get the details of the employees whose name starts with S
SELECT *
FROM Emp
WHERE Ename LIKE 'S%';

- 22. Get the details of the employees who work in Bangalore location
SELECT e.*
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE d.Loc = 'Bangalore';

- 23. Get the employee details whose name starts with any letter between A and K
SELECT *
FROM Emp
WHERE UPPER(LEFT(Ename, 1)) BETWEEN 'A' AND 'K';

- 24. Display the employees whose manager name is Stefen
SELECT e.*
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
WHERE m.Ename = 'Stefen';

- 25. List the name of the manager who has the maximum number of employees working under him
SELECT m.Ename AS Manager, COUNT(e.EmpNo) AS NumEmployees
FROM Emp e
JOIN Emp m ON e.Mgr = m.EmpNo
GROUP BY m.EmpNo, m.Ename
ORDER BY NumEmployees DESC
LIMIT 1;

- 26. Display the employee details, department details, and the manager details of the employee who has the second highest salary
SELECT e.*, d.Dname, d.Loc, m.Ename AS ManagerName
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
LEFT JOIN Emp m ON e.Mgr = m.EmpNo
ORDER BY e.Sal DESC
LIMIT 1 OFFSET 1;

- 27. List all details of all the managers
SELECT *
FROM Emp
WHERE EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL);

- 28. List the details and total experience of all the managers
SELECT m.*, TIMESTAMPDIFF(YEAR, m.Hire_Date, CURDATE()) AS Experience
FROM Emp m
WHERE m.EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL);

- 29. List the employees who are managers, take commission less than 1000, and work in Delhi
SELECT e.*
FROM Emp e
JOIN Dept d ON e.DeptNo = d.DeptNo
WHERE e.EmpNo IN (SELECT DISTINCT Mgr FROM Emp WHERE Mgr IS NOT NULL)
  AND COALESCE(e.Commission, 0) < 1000
  AND d.Loc = 'Delhi';

- 30. Display the details of employees who are senior to Martin
SELECT *
FROM Emp
WHERE Hire_Date < (SELECT Hire_Date FROM Emp WHERE Ename = 'Martin');
