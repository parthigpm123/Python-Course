

class cal():
      def __init__(self,num):
            self.num=num
            
      def __add__(self,others):
            
            return self.num+others.num
obj1=cal(10)
obj2=cal(10) 

print("Added Value:", obj1+obj2)           

         