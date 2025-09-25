/*ORDER BY clause is used to sort the result-set in ascending or descending order. By default it sorts the records in ascending order. To sort the records in descending order, you can use the DESC keyword.*/

SELECT * FROM studentrecords ORDER BY student_id ASC;

SELECT * FROM studentrecords ORDER BY student_id DESC;

SELECT * FROM studentrecords ORDER BY student_name ASC;

SELECT * FROM studentrecords ORDER BY student_name DESC;

SELECT * FROM studentrecords ORDER BY studentmarks ASC;

SELECT * FROM studentrecords ORDER BY studentmarks DESC;

SELECT * FROM studentrecords ORDER BY studentdepartment ASC;

SELECT * FROM studentrecords ORDER BY studentdepartment DESC;

SELECT * FROM studentrecords ORDER BY student_name ASC, studentmarks DESC;
