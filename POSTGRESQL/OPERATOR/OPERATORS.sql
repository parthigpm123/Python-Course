Operators in the WHERE clause
We can operate with different operators in the WHERE clause:

=	Equal to
<	Less than
>	Greater than
<=	Less than or equal to
>=	Greater than or equal to
<>	Not equal to
!=	Not equal to
LIKE	Check if a value matches a pattern (case sensitive)
ILIKE	Check if a value matches a pattern (case insensitive)
AND	Logical AND
OR	Logical OR
IN	Check if a value is between a range of values
BETWEEN	Check if a value is between a range of values
IS NULL	Check if a value is NULL
NOT	Makes a negative result e.g. NOT LIKE, NOT IN, NOT BETWEEN


1 Logical operators
Used to combine or negate Boolean expressions, often in a WHERE or HAVING clause. 
AND: Returns true if both conditions are true.
OR: Returns true if either condition is true.
NOT: Reverses the logical state of a condition. 

2 Comparison operators
Used to compare values. They are available for most data types where a sensible comparison can be made. 
=: Equal to.
<> or !=: Not equal to.
>: Greater than.
<: Less than.
>=: Greater than or equal to.
<=: Less than or equal to. 

3 Special comparison operators
IS NULL / IS NOT NULL: Checks for NULL values. Standard comparison operators like = and <> do not work with NULL.
IN / NOT IN: Checks if a value is present in a given list of values.
BETWEEN / NOT BETWEEN: Checks if a value is within a specified range, inclusive of the boundaries.
IS DISTINCT FROM / IS NOT DISTINCT FROM: Null-safe comparison. IS DISTINCT FROM treats NULL values as a comparable data value rather than "unknown". 


4 Arithmetic operators
Used for mathematical calculations on numeric data types. 
+: Addition.
-: Subtraction.
*: Multiplication.
/: Division.
%: Modulo (returns the remainder of a division).
^: Exponentiation.
|/: Square root.
||/: Cube root.
!: Factorial. 


5 Pattern matching operators
Used for matching string values against patterns. 
LIKE (~~): Case-sensitive pattern matching using wildcards % (any sequence of zero or more characters) and _ (any single character).
ILIKE (~~*): Case-insensitive version of LIKE.
~: Case-sensitive POSIX regular expression match.
~*: Case-insensitive POSIX regular expression match.
SIMILAR TO: SQL standard operator for pattern matching, falling between LIKE and regular expressions. 


6 Bitwise operators
Used for manipulating individual bits within integer and bit string data types. 
&: Bitwise AND.
|: Bitwise OR.
#: Bitwise XOR.
~: Bitwise NOT.
<<: Bitwise shift left.
>>: Bitwise shift right. 



7 Subquery operators
Used to evaluate conditions based on the results of a subquery.
ALL: Compares a value against every value returned by a subquery. For a condition to be true, it must be true for all values.
ANY / SOME: Compares a value against any value returned by a subquery. The condition is true if it is true for at least one of the values.
EXISTS: Returns true if the subquery returns at least one row, and false if it returns none.




8 Set operators
Used to combine the results of two or more SELECT statements.
UNION: Combines the result sets of two or more queries, removing duplicate rows.
UNION ALL: Combines the result sets of two or more queries, keeping all duplicate rows.
INTERSECT: Returns only the rows that are present in both result sets.
EXCEPT: Returns only the rows that are in the first result set but not in the second. 
AI can make mistakes, so double-check responses




Examples

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