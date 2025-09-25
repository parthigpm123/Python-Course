/*Aliases
SQL aliases are used to give a table, or a column in a table, a temporary name.

Aliases are often used to make column names more readable.

An alias only exists for the duration of that query.

An alias is created with the AS keyword.*/


SELECT student_id AS std_ID, student_name AS std_name, studentmarks AS MARKS, studentdepartment AS Dept FROM studentrecords;