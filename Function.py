'''
def add():
      a = int(input("Give Input : "))
      b = int(input("Give Input : "))
      print(a+b)
add()      

def sub():
      a=int(input("give input: "))
      b=int(input("give input: "))
      print(a-b)
sub()      




def myfunc():
 print("this is my function ")
myfunc()      
      

   
   
#find even or odd number by using function with user input
num = int(input("Give any input"))

def evenorodd():
      if(num%2==0):
            print("even")
      else:
            print("odd")
evenorodd()            



# return function example
def add_pannu(a,b = 10):
      result=a+b
      return result
output=add_pannu(30,  20)
print(output)       


def sum1(*numbers):
      result = sum(numbers)
      return result
output = sum1(10,20,30,40,40,50,)
sum1()
print(output)


#PYTHON HAVE TWO TYPE OF FUNCTION 
#1 VOID FUCNTION

#2.NON-VOID FUNCTION

# 1void function example  WITHOUT RETURN TYPE
def void_func():
      print("Python Hello World")
void_func()


2# NON-VOID FUNCTION  WITH RETURN TYPE
#you can use outside of function
def non_void():
      z=10
      return z
print(non_void())


# SCOPE OF VARIABLE

# 1 GLOBAL VARIABLE

# 2 LOCAL vARIABLE 


#1 global variable YOU CAN USE INSIDE AND OUT SIDE OF FUNCTION
      
X ="awesome"
     
def glob():
      print('python is',X)
glob()           



#2 LOCAL VARIABLE YOU CAN ONLY USE IN INSIDE OF FUNCTION

# "global" keyword make local variable to global

def loc():
      global x
      x = 'fantastic '
      print('python is ',x)
loc()      

print(x)

'''
'''


# 5  TYPE OF PYTHON FUNCTION  

# 1 BUILT-IN FUNCTIONS
 LEN() TYPE() INPUT()
# 2 FUNCTION DEFINES IN MODULES 

#IMPORT MATH


# 3 USER DEFINE FUNCTION

#<==========================================>

# 5 TYPES OF ARGUMENTS

# 1 LITERAL VALUE ASSIGN

def myfunc(a,b):
      global c
      c = a+b
      return c  
print(myfunc(10,10))

print(c) 
      

# 2 PASSING VARIABLE 

def pass1(a,b):
      z=a+b
      print("the result is" ,z)
      return z
a=10
b=20
pass1(a,b)

print(pass1(a,b))  
print(pass1)

# 3 USER INPUT

# 4 CALL FUNCTION INTO PRINT STATEMENT

# 5 EXPRESSION INTO PRINT STATEMENT

'''
 
      