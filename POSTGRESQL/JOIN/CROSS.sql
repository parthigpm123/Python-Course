/*CROSS JOIN (Cartesian Product): This is a type of join operation that combines every row from the first table with every row from the second table. The result set contains a number of rows equal to the product of the number of rows in each table. It is used when there is no join condition specified, or when a complete combination of all rows between two datasets is desired.*/

Also called a Cartesian Join.

SELECT * FROM studentrecords CROSS JOIN employee;