'''A decorator in Python is a special type of function used to modify or enhance the behavior of another function or method without changing its actual code.

Think of it as wrapping extra functionality around an existing function.  
'''

"""Complicated Decorator Example"""
"""decorator without parameters"""



def strupper(func):
      def inner():
            str1=func()
            return str1.upper()
      return inner
#-----------------------------
def printstr():
      return "hello world"

print(printstr())#upper case

obj=strupper(printstr) #function are reference

print(obj())#upper case





''' Simple Decorator Example'''

def strupper(func):

      def inner():
            str1=func()
            return str1.upper()
      return inner
      


@strupper
def printstr():
      return "hello world"


print(printstr())#upper case
'''
obj=strupper(printstr) #function are reference

print(obj())#upper case'''



"""decorator without parameters"""
def outer(func):
      def inner(x,y):
            if y==0:
                  return "Give value greater than zero"
            return func(x,y)
      return inner
            

@outer
def div(a,b):
      return a/b
print(div(10,0))




