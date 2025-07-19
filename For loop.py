'''
The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or dictionary) or other iterable objects. It allows you to execute a block of code for each item in the sequence. 
Basic Syntax:
Python

for variable in sequence:
    # block of code to be executed for each item
Explanation:
for keyword: Indicates the start of a for loop.
variable: A temporary variable that takes on the value of each item in the sequence during each iteration of the loop.
in keyword: Used to link the variable to the sequence you want to iterate over. 
sequence: The iterable object (e.g., a list, tuple, string, or range object) that the loop will iterate through.
Colon (:): Marks the end of the for loop header.
Indented Block of Code: The statements indented below the for loop header are executed repeatedly for each item in the sequence. Indentation is crucial in Python to define the scope of the loop.
Examples:
1. Iterating over a list:
Python

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#2. Iterating over a string:
#Python

for char in "Python":
    print(char)
#3. Using range() for a fixed number of iterations:
#Python

for i in range(5):  # Iterates from 0 to 4
    print(i)
#4. Iterating with enumerate() to get both index and value:
#Python

my_list = ["a", "b", "c"]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

Control Flow Statements within for loops:
break: Exits the loop entirely.
continue: Skips the current iteration and moves to the next.
else (with for loop): The else block is executed only if the loop completes without encountering a break statement. 




for me in range(5):
      print("troll geak ")
      

 #String Loop 
      
for i in "apple":
    print(i)
    
 # Int Loop in Range function
for x in range(6):
     print(x)   
     
     
# range function  with start and end     
for y in range(1,7):
    print(y)       

# 6 Table in range function

for z in range(1,11):
    print("7x",z,"=",7*z)
    
    
    
# user input in for loop    
a= int(input("Enter input no "))
b= int(input("Enter input no "))

for c in range(a,b):
    print(c)


#even numbersin for loop

for m in range(1,11):
    if m%2==0:
     print(m)



# Nested Loops
for i in range(1,3):
    print("week:",i)
    for j in range(1,4):
        print("day:",j)   
      '''
 
for i in range(1,2):
    print("*",i)
    for j in range(1,2):
        print("**",j)   
    for k in range(1,2):
        print("***",k)
    for l in range(1,2):
        print("****",l)
        
        
for i in range(1,2):
    print("*")
    for j in range(1,2):
        print("**")   
    for k in range(1,2):
        print("***")
    for l in range(1,2):
        print("****")
         
      