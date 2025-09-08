'''
1. Arithmetic Operator Overloading

You can redefine how arithmetic operators behave.

Operator	Method Name
+	__add__(self, other)
-	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)

string and number concatenate =__str__()


'''

class cal():
      def __init__(self,num):
            self.num=num
            
      def __add__(self,others):
            
            return self.num+others.num
obj1=cal(10)
obj2=cal(10) 

print("Added Value:", obj1+obj2)           



'''string and number concatenate =__str__()'''
         
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)
print(p)         