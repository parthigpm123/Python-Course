'''There are three type of Methods in python oops

1.Instance Method

2.Class Method

3.static method


'''

'''1.Instance Methods'''
print('This is instance method')
class Dog:
    def __init__(self, name):   # Constructor
        self.name = name        # Assigns name to the object

    def bark(self):             # Instance method
        print(f"{self.name} says Woof!")

# Create object
my_dog = Dog("Buddy")

# Call instance method
my_dog.bark()
print("Instance method completed\n")
#-----------------------------------------------------#

''' 2.Class Method'''  
print("This is Class Method")
class animal():
            species="dog"
            @classmethod
            def get_species(cls):
                  return cls.species
an=animal()
print("The Animal Name is:",an.get_species())            
print("class method completed\n")           
#------------------------------------------#

print("This is static method") 

class static():
      
      @staticmethod
      def add(a,b):
            return a+b 
result=static.add(10,10)

print("Added Result:",result)      
                
print("Static Method Completed\n")                
#--------------------------------------#
            
            
print('This instance, class and static  mixed:')            
class laptop():
      charger_type="B-Type"
      def __init__(self):
            self.brand=""
            self.price=40
      def set_price(self,price):
            self.price=price
            self.brand=""
      def get_price(self):
            print("Price:",self.price)
            '''classmethod'''     
      @classmethod       
      def change_charger_type(cls):
           c=cls.charger_type="c-type"
           print("Charger type:",c)
      
      '''Static Method'''
      @staticmethod  
      def info():
            print("This is static method")      
              
hp=laptop()


hp.set_price(40000)
hp.get_price()
laptop.change_charger_type()

laptop.info()
print('completed!')





