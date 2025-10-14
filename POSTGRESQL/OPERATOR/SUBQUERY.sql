7 Subquery operators
Used to evaluate conditions based on the results of a subquery.

ALL: Compares a value against every value returned by a subquery. For a condition to be true, it must be true for all values.

ANY / SOME: Compares a value against any value returned by a subquery. The condition is true if it is true for at least one of the values.

EXISTS: Returns true if the subquery returns at least one row, and false if it returns none.
