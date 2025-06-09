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