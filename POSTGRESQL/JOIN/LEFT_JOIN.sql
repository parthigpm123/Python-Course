/* Example of LEFT JOIN in PostgreSQL Retrieving All Records from Left Table and Matching Records from Right Table */

select * from studentrecords left join car on studentrecords.student_name = car.carname;