SELECT * FROM car
WHERE carname = 'Toyota';

SELECT * FROM car
WHERE carmodel < 2026;

SELECT * FROM car
WHERE carmodel > 1975;

SELECT * FROM car
WHERE carmodel <= 1975;

SELECT * FROM car
WHERE carmodel >= 1975;

SELECT * FROM car
WHERE carmodel <> 1975;

SELECT * FROM car
WHERE carname = 'Toyota' AND carmodel = 2025;

SELECT * FROM car
WHERE carname = 'Toyota' OR carmodel = 2026;

SELECT * FROM car
WHERE carname IN ('Toyota', 'BMW');


SELECT * FROM car
WHERE carmodel IS NULL;

SELECT * FROM car
WHERE carname NOT LIKE 'B%';


SELECT * FROM car
WHERE carname NOT IN ('Volvo', 'Mercedes', 'Ford');

SELECT * FROM car
WHERE carmodel IS NOT NULL;