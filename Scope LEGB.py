


'''
A variable is only available from inside the region it is created. This is called scope.


L E G B

1 Local Scope

A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.


2 Enclosing Scope

3 Global Scope

A variable created in the main body of the Python code is a global variable and belongs to the global scope.

Global variables are available from within any scope, global and local.

4 built in method


Global Keyword
If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

The global keyword makes the variable global.

Example
If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 300

myfunc()

print(x)
'''




def myvar():
      a = "python is very easy language"#local variables 
      print(a)
myvar()      




#global variales you can access anywhere
y = "python is  awesome"

def cart():
      print('my',y)
cart()      
       







# enclosing scope example
def myfunc():
      x=("my name is")
      print(x)
          
      
      def myname():
            print(x, 'parthiban')
            
      myname()

myfunc()
                 



#built in variables functions and methods
'''
print(__name__)

print(__doc__)

print(__file__)

print(__package__)

print(__builtins__)
'''


delivery_partner="swiggy"

def hotel():
      item = 'pizza'
      
      def order():
            quantity =2
            print(f"ordering {quantity} {item} using {delivery_partner}")
      order()
   
hotel()    

# global keyword in function

def myfunc():
  global x
  x = 300

myfunc()

print(x)