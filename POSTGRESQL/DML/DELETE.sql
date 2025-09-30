/*🟢 1. DELETE → remove selected rows
-- Remove only BMW
DELETE FROM car WHERE carname = 'BMW';

-- Check table after delete
SELECT * FROM car;


👉 Only rows matching the condition are gone. Other cars stay.*/

-- Another way to write the same command
delete from cars where carname = 'BMW'; -- delete rows where carname is BMW