'''
a = 10
if 10<a:
      print("smaller than a")
elif 10>a:
      print("greater than a") 
else:
      print("both are equal")



A = {'apple' , 'orang' , 'banana'}
b= {"pineapple","orang", "mango","kiwi"}

A.update(b)
print(A)      


A ={ 1,2,3}
b= {4,5,6}

A.update(b)
print(A)
 '''

#thislist =list( 'apple ','orange','kiwi','mango')
#print(type(thislist))


'''
set1 ={
      "name": "parthiban"
}

x=set1.get('name')
print(x)


set1 = {
      "name": "Name========> parthiban "
        
      }
x = set1.get("name")
print(x)


username = "parthiban"
password = 12345  

uname=input("Username : ")
pwd = int(input("password : "))

def myfunc():     
      print(username==uname and password==pwd)
      
myfunc()


username = "parthiban"
password = 12345  

uname=str(input("Username : "))
pwd = int(input("password : "))

def validate():
      if(username==uname and password==pwd):
       print("both are same")
      else:
       print("not true")
validate()
            


class ooty:
      def botanical(self):
          print("for research")
      def boathouse(self):
          print("let's party")
parthiban=ooty()
vijay=ooty()
parthiban.botanical()
vijay.boathouse()

class calculator:
            def input(self,a,b):
                  print( a + b)
            def sub(self,a,b):
                  return a -b
            def mul(self,a,b):
                  return a*b
            def div(self,a,b):
                  return a /b


class student:
    def __init__(self):
            self.name = "parthiban"
            self.age = "24"
            a = self
            print(a)
s1=student()


class goa:
      name = " "
      drink = ""
      def party(self):
            print("let's party.........")
      def beach(self):
            print("lets enjoy beach...")
            
ramesh = goa()  
suresh =goa()          
            
            
ramesh.party()
suresh.beach()      
            
            
            
                   




ramesh.name = "ramesh" 
suresh.name = "suresh"

ramesh.drink = "wine"

suresh.drink = "beer"
 

print(ramesh.name) 
print("drinks:",ramesh.drink)               
print(suresh.name)


print("drinks:",suresh.drink) 

         
                        



lst =["python","hello","world","fantastic","super"]

itr =iter(lst)
print(itr)



def add(a,b):
      print(a + b)
      
      
         
def greeting(name):
      print("hello" + name)



try:
    a = int(input("enter no"))
    b = int(input("enter no"))
    
    print(a-b)
except: 
    print("Error Occurred")
else:
      print("result successful")    
      
      
try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise ValueError("Age cannot be negative")
    
    print("Your age is:", age)

except ValueError as e:
    print("Error:", e)

 
import time
x =time.localtime()

print("year", x.tm_year)
print("month", x.tm_mon)
print("day", x.tm_mday)
print("hour", x.tm_hour)
print("minute", x.tm_min)
print("second", x.tm_sec)
print("hello")


def add():
      a=int(input('enter'))
      b=int(input("enter"))
      c=a+b
      return c
result=add()
print(result)



for x in range(1,11):
      
     print('5 tables')
a=int(input("Enter Number : "))
'''
'''
print("last polymorphism")               
                       
class employee():
      def __init__(self,name,salary):
       self.name=name
       self.salary=salary
       
class manager(employee):
        def __init__(self,department,name,salary):
         super().__init__(name,salary)
         self.department=department 
         
        def display(self):
              print(self.name,self.salary,self.department)
            
  
q1=manager("h",5000,"hr")
q1.display()


class animal():
      def sound(self):
       print("Animal makes Sound")
class dog(animal):
      def sound(self):
            print('Dog barks')     
            
class bird(animal):
      def sound(self):
            print("birds sings")               
b1=bird()
b1.sound()  

while True:
      
      try:  
         a = int(input("Enter Table Number : "))
         for i in range(1,11):
          print(i,'x',a,'=',i*a)
      except:
            print("Enter A integer value")       
            
'''
'''#even or odd
list1 = [1,2,3,4,5,6,7,8,9,0]
even_number=[]
ODD_numbers=[]
for i in list1:
      if(i%2==0):
            even_number.append(i)
      elif i%2==1:
            ODD_numbers.append(i)
print('EVEN_NUMBERS:',even_number,'\n','ODD_NUMBERS',ODD_numbers)                       
'''
    
    
    
      
 
''' 
n = [1,2,3,-1,-3,-6,-7,-9]           
         
for x in n:
      if x>0:      
            print(f'{x} is Positive Numbers')
      elif x<0:
            print(x,'is negative numbers')
'''  
'''      
# Match case statement
number=int(input("Enter Number:"))  
          
match number:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
'''
'''#FOR_LOOP Condition
list1 =[1,2,3,4,5,6,7,8,9,0,
'Apple','Orange','Banana']

#Iteration
for i in list1:
      print(i)
'''
'''
i=10
while i>0:
      print(i,end='\n')
      i=i-1
      
      
      
print('\n')      
num=int(input("ENTER TABLE NUMBER: "))      
i=1
while i<=10:
      print('\n',i,'x',num,'=',i*num,)
      i=i+1      
'''
'''
while True:
 try:
  table_num=int(input("ENTER TABLE NUMBER: " ))
 
  for i in range(1,11):
      print(i,'x',table_num,'=',i*2)
 except:
      print("Something error")
 else:
      print('successful completed success')       
'''
   
   
   
                                      
#BASIC CLASSES AND OBJECT                                
class calculator():
      def __init__(self,a,b):
            self.a=a   
            self.b=b
      def cal(self):
            self.a , self.b
            print("Added Value=         ",self.a+self.b)
            print("subtract value=      ",self.a-self.b)
            print("multiplication value=",self.a*self.b)
            print("division value=      ",self.a/self.b)
      
cal1=calculator(10,10)
cal1.cal()                        
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      