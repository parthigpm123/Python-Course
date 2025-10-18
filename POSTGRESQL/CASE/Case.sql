SELECT student_name,studentmarks,

CASE
    WHEN studentmarks >= 90 THEN 'A+'
    WHEN studentmarks >= 80 THEN 'A'
    WHEN studentmarks >= 70 THEN 'B+'
    WHEN studentmarks >= 60 THEN 'B'
    WHEN studentmarks >= 50 THEN 'C'
    ELSE 'Fail'
END AS finalgrade
FROM studentrecords