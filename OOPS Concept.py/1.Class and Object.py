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
'''


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
