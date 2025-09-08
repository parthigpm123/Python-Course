'''Method overloading'''                           
class calculator():
      def sum1(self,*args):
            total=0
            for i in args:
                  total+=i
            print("Added Value Result:",total)
obj=calculator()
obj.sum1(10,10)              