
'''Types of variables in the class '''

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