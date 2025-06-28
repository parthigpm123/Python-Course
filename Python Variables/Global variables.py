#this is a global variable access from anywhere in the code
y = "python"

def myfunc():
      print(y)
myfunc()



#this local variable is only accessible within function
def myfunc():
      global x
      x = "programming"
      print(x)
myfunc()
  
print(x)  

def myvar():
      x = "python is awesome"
      
      def cart():
            print(x)
            
      cart()
 
myvar()  


def myvar():
      global x
      x="python is awesome"
      global y
      y="python is great"
      print()
myvar()

print(x)  
print(y)             
        