#[expression for item in iterable]

'''List comprehension in Python is a concise and efficient way to create new lists based on existing iterables (like lists, tuples, ranges, or strings). It offers a more compact and readable syntax compared to traditional for loops for tasks involving list creation, transformation, or filtering.
The general syntax of a list comprehension is:
Python

new_list = [expression for item in iterable if condition]
Explanation of components:
expression: This is the operation applied to each item that satisfies the condition. It determines the value that will be added to the new_list.
for item in iterable: This is the loop that iterates through each item in the iterable.
if condition (optional): This is a conditional statement that filters the items. Only items for which the condition evaluates to True will be processed by the expression and included in the new_list.'''

arr =[1,2,3,4,5,6,7,8,9,10]

odd=[i for i in arr if i%2 !=0]
print(odd)

