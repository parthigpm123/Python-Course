In PostgreSQL, the HAVING clause is used to filter groups of rows that have been created by the GROUP BY clause. It is distinct from the WHERE clause, which filters individual rows before grouping occurs. The HAVING clause allows you to specify conditions on aggregate functions.
Here is the general syntax for using the HAVING clause in PostgreSQL:
Code

SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition_on_individual_rows -- Optional
GROUP BY column1
HAVING condition_on_groups -- Condition involving aggregate functions
ORDER BY column1; -- Optional

Explanation:
SELECT column1, aggregate_function(column2): Specifies the columns to be retrieved, including at least one aggregate function (e.g., SUM(), COUNT(), AVG(), MIN(), MAX()).
FROM table_name: Indicates the table from which data is being retrieved.
WHERE condition_on_individual_rows (Optional): Filters individual rows before they are grouped.
GROUP BY column1: Groups the rows based on the values in column1. All rows with the same column1 value will form a single group.
HAVING condition_on_groups: Filters the groups created by GROUP BY. This condition typically involves aggregate functions and specifies criteria that the aggregated results must meet.
ORDER BY column1 (Optional): Sorts the final result set.