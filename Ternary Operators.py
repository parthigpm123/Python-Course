'''
The ternary operator is a one line shorthand for if else statement.

basic syntax:
value_if_true if condition else value_if_false

'''
age =19

print("child" if age < 18 else "Adult")


age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)   # Output: Adult


ag=int(input('Enter Your Age=>'))

check="Adult" if ag >= 18 else "Child"

print("your age is",ag,"you are",check)