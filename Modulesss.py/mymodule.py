def add(a,b):
      print(a + b)
         
def greeting(name):
      print("hello" + name)
      
 #define return function       
def module(a,b,c,d):
      result = a+b,c-d 
      return result



   # calculator function import from calculator file    
      
import calculator as cal  

result =cal.add(10,40)
print("result=>", result)

result =cal.sub(10,10)
print("result=>", result)  

result=cal.mul(10,2)
print("result=>", result)

result=cal.div(10,5)
print("result=>", result)

#directly access function in other file

from calculator import add

res = add(10,10)
print(res)

