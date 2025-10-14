8 Set operators
Used to combine the results of two or more SELECT statements.

UNION: Combines the result sets of two or more queries, removing duplicate rows.

UNION ALL: Combines the result sets of two or more queries, keeping all duplicate rows.

INTERSECT: Returns only the rows that are present in both result sets.(common rows)

EXCEPT: Returns only the rows that are in the first result set but not in the second.

Examples


In PostgreSQL (psql), set operators are used to combine the results of two or more SELECT queries.
The main set operators are:

UNION

UNION ALL

INTERSECT

EXCEPT

Let’s go through each with examples 👇

🔹 Create Sample Tables
CREATE TABLE students_a (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE students_b (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO students_a (name) VALUES 
('Alice'), ('Bob'), ('Charlie');

INSERT INTO students_b (name) VALUES 
('Bob'), ('David'), ('Eve');
1️⃣ UNION — combines results and removes duplicates
SELECT name FROM students_a
UNION
SELECT name FROM students_b;
Output:

 name
--------
 Alice
 Bob
 Charlie
 David
 Eve
✅ Removes duplicates (Bob appears only once).

2️⃣ UNION ALL — combines results and keeps duplicates
SELECT name FROM students_a
UNION ALL
SELECT name FROM students_b;
Output:

 name
--------
 Alice
 Bob
 Charlie
 Bob
 David
 Eve
✅ Keeps duplicates.

3️⃣ INTERSECT — returns common rows from both queries
SELECT name FROM students_a
INTERSECT
SELECT name FROM students_b;
Output:

 name
--------
 Bob
✅ Shows only names present in both tables.

4️⃣ EXCEPT — returns rows from the first query that are not in the second
SELECT name FROM students_a
EXCEPT
SELECT name FROM students_b;
Output:

 name
--------
 Alice
 Charlie
✅ Shows names only in students_a (not in students_b).

⚙️ Notes
All participating SELECT queries must have the same number of columns and compatible data types.

You can use ORDER BY at the end of the full statement:

SELECT name FROM students_a
UNION
SELECT name FROM students_b
ORDER BY name;
Would you like me to show a real-world exa