def fun1():
      print("Hi...i am function 1")
def fun2(func):
      print("Hi i am function2 ...calling function 1")
      func()
      
fun2(fun1)            
      