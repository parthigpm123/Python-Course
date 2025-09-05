'''
python is an object oriented programming language allowing you to 
structure your code using classes and object  for better organization and reusability

==> python provide clear structure to program 

===>makes your code easier to maintain

==>reuse and debug

===>don't repeat your code 

==> reusable for code

# what is class and object

#class     #object
car===>    volvo,audi 
fruit==>   apple,orange,mango

'''
'''
#class is a template

class car:
      no_of_wheels = 4 #member variables
      mileage =20.0
      no_of_airbags=5
  #------------------------------------------------#    
      def moveforward(self):
       print("car is moving forward!")    #member method
      
      def movebackward(self):
       print("car is moving backward!")
 #--------------------------------------------------#      
       
car1 = car#instance of class -object instantiation      

print(car1.no_of_wheels)

print(car1.mileage)


car2 =car
print("mileage==>",car2.mileage)

car2.mileage = 25.0

print(car2.no_of_airbags)
print("mileage==>",car2.mileage)

car2 = car()
car2.moveforward()


class Bank_account:
      customer_name = " parthiban"
      balance = 1000.49
      account_number = "9**********"




Bank_account1 = Bank_account()


Bank_account1.customer_name= "vicky"
print(Bank_account1.customer_name)




class  car:
      car_name  = "volvo"
      model =    "1986"
      price = "200000"
      seat = 5
      
car1 = car

print(car1.seat)

print(car1.price)
car1.price = 30   
                  
print(car1.price)                 

class pondy():
      name=""
      drink=""
      def enjoy(self):
            return "Let's Enjoy Party"
      def study(self):
       return "study purpose"      

vijay=pondy()
parthiban=pondy()
#----------------------------#
vijay.name="vijay"
vijay.drink="hot and bear"
parthiban.drink="bear only"
#---------------------------------#
print(vijay.name)
b=vijay.enjoy()
print(b)
print(vijay.drink)
#-------------------------------------------#
parthiban.name="parthiban"
print("\n",parthiban.name)
a=parthiban.enjoy()
print(a)
print(parthiban.drink)



class laptop():
      price=0
      processor=""
      Ram=""

HP=laptop()
Dell=laptop()
Lenovo=laptop() 

HP.price=40000
HP.processor="i5"
HP.ram="16gb ram"     

Dell.price=50000
Dell.processor="i7"
Dell.ram="8gb"
#-----------------------------------------#

print("\nHP Laptop Details!")
print("Hp Laptop Price    :",HP.price)
print("Hp processor Price :",HP.processor)
print("Hp Ram Price      :",HP.ram,"\n")

#-------------------------------#

print("Dell Laptop Details!")
print("Dell Laptop Price:",Dell.price)
print("Dell Processor   :",Dell.processor)
print("Dell ram size    :",Dell.ram) 

'''
'''Constructor and self Keyword'''
'''
class laptop:
      def __init__(self):
      # print('def init=',"hello world")
       self.price=5000000
       self.processor="kjjhjgk"
       self.ram="kgggfy"
      def display(self):
            print("dell price=",self.price)
            print("dell processor=",self.processor)
            print("dell ram",self.ram)
             

hp=laptop()

dell=laptop()
      

hp.price=40000
hp.processor="i5"
hp.ram="16gb" 

dell.price="60000"
dell.processor="i9"
dell.ram="32gb"
       
hp.display()       
       
dell.display()


print("----------------------------------------------")

#value change while object create inside arguments giving
class fruits():
      def __init__(self,col):
            self.color=col

mango=fruits("yellow")            
            
print(mango.color)            
print("#---------------------------------------------#")


print("Faculty Details")
class teacher:
      def __init__(self,nam,reg):
            self.name=nam
            self.regno=reg
            
      def display(self):
            print("Teacher Name:",self.name)
            print("The Register No:",self.regno)
t1=teacher("Mala",6374)
t2=teacher("malar",1234) 

t1.display()
t2.display()                 
            
            
class calculator():
      def __init__(self,a,b):
            self.a=a   
            self.b=b
      def add(self):
            #print("Added Value=         ",self.a+self.b)
            #print("subtract value=      ",self.a-self.b)
            #print("multiplication value=",self.a*self.b)
            #print("division value=      ",self.a/self.b)
            x=self.a+self.b
      
            return x
      
cal1=calculator(10,10)

                     
print(cal1.add())


class car():
      def __init__(self,wheels,airbags,mileage):
            wheels,self.wheels=wheels
            self.airbags=airbags
            self.mileage=mileage
            
car1=car(4,3,70)            

print(car1.wheels)
'''

'''Types of variables in the class '''
'''
class phone():
      charger_type="B-type"
      charger_type="C-Type"
        #class Variables
      
      def __init__(self,brand,price):
            self.brand=brand
            self.price=price #instance variable
      def display(self):
            
                   
            print("Brand:",self.brand)
            print("Price:",self.price)
            print("Charger type",self.charger_type) 
phone.charger_type="A-type"             
samsung=phone("samsung",10000)
samsung.display()

print("\n")
redmi=phone("Redmi",40000)
redmi.display()

print("\n")

google=phone("Google Pixel",50000)
google.display()
'''


'''Types of methods in class'''

class laptop():
      Charger_type="B-Type"
      def __init__(self):
            self.brand=""
            self.price=40
      def set_price(self,price):
            self.price=price
            self.brand=""
      def get_price(self):
            print("Price:",self.price)            
hp=laptop()


hp.set_price(40000)
hp.get_price()            