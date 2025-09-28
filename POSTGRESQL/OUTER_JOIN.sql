SELECT * FROM studentrecords
FULL OUTER JOIN car
ON studentrecords.student_name = car.carname;