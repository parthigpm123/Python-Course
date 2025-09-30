UPDATE cars
SET carmodel = '2025'
WHERE carname = 'BMW';
UPDATE car
SET carseat = '4'
WHERE carname = 'BMW';

UPDATE cars
SET carseat = '4'
WHERE carname IN ('Audi', 'Mercedes', 'Toyota', 'Honda');

UPDATE cars
SET carmodel = '2025'
WHERE carname IN ('Audi', 'Mercedes', 'Toyota', 'Honda');