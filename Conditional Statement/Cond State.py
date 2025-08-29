#what is statement?
'''Instructions given to computer'''

'''There three types of statements

1. simple statement
2 .compound statement
3. empty statement'''


'''
Compound Statement:

A compound statement represents a group of statements that are executed as a single unit.

They typically consist of a header followed by an indented body containing one or more simple or other compound statements.

Examples include conditional statements (if, elif, else), looping statements (for, while), function definitions (def), class definitions (class), and exception handling blocks (try, except, finally).
'''
x=10

if x > 5: # Compound statement header
        print("x is greater than 5") # Indented body
else:
        print("x is not greater than 5")




# conditional statement        
a=5

b=int(input("Enter the number===>"))        
if a==b:
      print("a equals to b")
      print('program successful runs!!!')
elif b==6:
      print("b is 6")      
      
else:
      print("a is not equal to b")
      print("program failed!!!")               
      
     
     
num = int(input("Enter the number==>"))

if num > 0:
      print("positive Number!!!")
elif num == 0:
      print("zero")      
else:
      print("Negative Number!!!")            
print("done")      
      
      
x = 5
y= 10

if x>y:
      largest =x
else:
      largest=y
      print("laregest number is===>",largest)            