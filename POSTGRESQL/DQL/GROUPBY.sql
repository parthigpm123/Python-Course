/*GROUP BY
The GROUP BY clause groups rows that have the same values into summary rows, like "find the number of customers in each country".

The GROUP BY clause is often used with aggregate functions like COUNT(), MAX(), MIN(), SUM(), AVG() to group the result-set by one or more columns.*/





select sum(Studentmarks),
Studentdepartment 
from studentrecords 
group by Studentdepartment;




