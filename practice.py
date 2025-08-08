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
 '''
 
import time
x =time.localtime()

print("year", x.tm_year)
print("month", x.tm_mon)
print("day", x.tm_mday)
print("hour", x.tm_hour)
print("minute", x.tm_min)
print("second", x.tm_sec)
print("hello")

     