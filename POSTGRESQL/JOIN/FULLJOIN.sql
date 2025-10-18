/* Example of FULL JOIN in PostgreSQL Retrieving All Records When There is a Match in Either Left or Right Table */
SELECT * FROM studentrecords
FULL OUTER JOIN car
ON studentrecords.student_name = car.carname;