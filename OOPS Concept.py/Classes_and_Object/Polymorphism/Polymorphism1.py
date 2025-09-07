'''Key aspects of polymorphism in Python:
Method Overriding: This is a common form of polymorphism in inheritance. Subclasses can provide their own specific implementation of a method that is already defined in their superclass. When the method is called on an object of the subclass, the overridden version is executed.'''

'''
class animal():
      def sound(self):
       print("Animal makes Sound")
class dog(animal):
      def sound(self):
            print('Dog barks')     
            
class bird():
      def sound(self):
            print("birds sings")               
b1=bird()
b1.sound()


'''#child class override base class'''
class shape():
      def area(self):
            return 0
class rectangle(shape):
      def area(self):
            l=10
            w=10
            print("Area of rectangle:",l*w)
r1=rectangle()
r1.area() 

"""
'''super keyword'''
class person():
      def __init__(self,name):
            self.name=name
            
            
class student(person):
      def __init__(self,name,grade):
            super().__init__(name)
            self.grade=grade
            
            
      def display(self):
            a=print("name:",self.name,"Grade:",self.grade)
            
            
s1=student("vijay","A") 

s1.display()  
"""
   

'''method override polymorphism'''
class vehicle():
      def start(self):
            print('Vehicle started')
class car(vehicle):
      def start(self):
            print("car started")
car1=car()
car1.start()   





        
               
print("last polymorphism")               
                       
class employee():
      def __init__(self,name,salary):
       self.name=name
       self.salary=salary
class manager(employee):
        def __init__(self,name,salary,department):
         super().__init__(name,salary)
         self.department=department 
        def display(self):
              print("Name:",self.name,"Salary:",self.salary,"Department:",self.department)
            
  
q1=manager("parthiban",50000,"developer")
q1.display()

           
                           
      