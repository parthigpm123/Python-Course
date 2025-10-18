The CASE statement in SQL provides conditional logic, allowing different values to be returned based on specific conditions. It functions similarly to IF-THEN-ELSE statements found in other programming languages.

⚙️ In Short:
Keyword	Purpose
CASE	Starts the condition block
WHEN	Defines a condition
THEN	Defines what to return if true
ELSE	Default result if no condition matches
END	Closes the CASE expression


💡 Basic Syntax:
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE result3
END


✅ The CASE checks each condition in order:

If a condition is true, it returns the value after THEN.

If no condition matches, it returns the value after ELSE.

The END keyword marks the end of the CASE expression.

🔹 Example 1: Simple CASE
SELECT name, marks,
CASE
    WHEN marks >= 90 THEN 'Excellent'
    WHEN marks >= 75 THEN 'Good'
    WHEN marks >= 50 THEN 'Average'
    ELSE 'Fail'
END AS grade
FROM students;


🧠 Explanation:

If marks >= 90, grade = Excellent

If marks >= 75, grade = Good

If marks >= 50, grade = Average

Otherwise, grade = Fail
