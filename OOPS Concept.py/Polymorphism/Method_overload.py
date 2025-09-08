'''Method overloading'''
                     
class calculator():
      def sum1(self,*args):
            total=0
         
            for i in args:
                  total+=i
                  
            print("Added Value Result:",total)
obj=calculator()
obj.sum1(10,10)              
obj.sum1(10,30)              
obj.sum1(10,40)              


class calculator():
    def __init__(self):
        self.count = 0  # Initialize count

    def sum1(self, *args):
        self.count += 1  # Increment count per call
        total = sum(args)  # Sum all arguments
        print(self.count, "Added Value Result:", total)

obj = calculator()
obj.sum1(10, 10)   # 1 Added Value Result: 20
obj.sum1(10, 30)   # 2 Added Value Result: 40
obj.sum1(10, 40)   # 3 Added Value Result: 50
