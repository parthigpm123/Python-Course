def fun1():
      print("Hi...i am function 1")
def fun2(a):
      print("hi i am func 2 ...calling function 1")
      a()
      
fun2(fun1)            
      