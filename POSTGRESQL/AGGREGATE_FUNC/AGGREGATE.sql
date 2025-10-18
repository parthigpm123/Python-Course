An aggregate Function is a Function that performs a calculation on a set of values and returns a single value. Aggregate functions are often used with the GROUP BY clause of the SELECT statement.
/*🔹 Common Aggregate Functions 5

Function	Description	Example:

COUNT()Counts number of rows	SELECT COUNT(*) FROM students;
SUM()	Adds up values in a column	SELECT SUM(marks) FROM students;
AVG()	Returns average value	SELECT AVG(marks) FROM students;
MAX()	Returns highest value	SELECT MAX(marks) FROM students;
MIN()	Returns lowest value	SELECT MIN(marks) FROM students;
*/

select count(studentrecords) from studentrecords;

select sum(studentmarks) as Totalmarks from studentrecords;

select avg(studentmarks) from studentrecords;

select max(studentmarks) from studentrecords;

select min(studentmarks) from studentrecords;
