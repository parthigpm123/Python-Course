
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