/*Table Structure change*/
/* colomn add */
/* remove colomn */
/* colomn data type change */
/* modify colomn size */

ALTER TABLE cars
ALTER COLUMN carname TYPE VARCHAR(10);

alter table cars
alter column carmodel type varchar(100);


/*delete colomn*/
ALTER TABLE cars
DROP COLUMN carmodel;

/*add colomn*/
ALTER TABLE cars ADD COLUMN carmodel VARCHAR(50);



ALTER DATABASE old_database_name
RENAME TO new_database_name;




