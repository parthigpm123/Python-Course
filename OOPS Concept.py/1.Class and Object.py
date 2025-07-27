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

      
