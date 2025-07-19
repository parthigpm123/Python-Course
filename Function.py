'''
def add():
      a = int(input("Give Input : "))
      b = int(input("Give Input : "))
      print(a+b)
add()      

def sub():
      a=int(input("give input: "))
      b=int(input("give input: "))
      print(a-b)
sub()      




def myfunc():
 print("this is my function ")
myfunc()      
      

   
   
#find even or odd number by using function with user input
num = int(input("Give any input"))

def evenorodd():
      if(num%2==0):
            print("even")
      else:
            print("odd")
evenorodd()            



# return function example
def add_pannu(a,b = 10):
      result=a+b
      return result
output=add_pannu(30,  20)
print(output)       

'''
def sum1(*numbers):
      result = sum(numbers)
      return result
output = sum1(10,20,30,40,40,50,)
sum1()
print(output)
