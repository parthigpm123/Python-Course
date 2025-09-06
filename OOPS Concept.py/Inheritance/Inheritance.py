'''There is 5 type of Inheritance

1 Single Inheritance

2 Multiple Inheritance

3 Multi-level Inheritance

4 Hierarchy Inheritance

5 Hybrid Inheritance

'''
'''
#single inheritance
class dad():
      def phone(self):
            print("This dad's phone")

class son(dad):
      def money(self):
            print("This is my money")

ram=son()

ram.phone()
ram.money()     
'''

#multiple inheritance
'''
class dad():
      def property(self):
            print("This is Dads property")
class mom():
      def car(self):
            print("This is mom's Car")
class son(mom,dad):
      def ball(self):
            print("this is my ball")
vijay=son()
vijay.property()
vijay.car()
'''

#Multi-Level Inheritance
'''
class grandpa():
      def phone(self):
            print("This is grandpa phone")                        
class dad(grandpa):
      def money(self):
            print("This is dads money")               
class son(dad):
      def laptop(self):
            print("This is my laptop")
sam=son()
sam.money()       

dad1=dad()
dad1.phone()                  2     czxw vcbnjv]ZY             
sam.phone()            
'''

#Hierarchy Inheritance
'''access 1 dad property multiple son  son1 son2 son3'''

class dad():#parent Class
      def money(self):
            print("this is dads money")
class son1(dad):#child class
      pass

class son2(dad):
      pass
class son3(dad):
      pass            
s1=son3()
s1.money()                        

#Hybrid  inheritance
            
             
'''Hybrid inheritance

=>The hybrid inheritance is combination of more than two or more type of inheritance 

=>combined=single,multi-level,multiple inherit,hierarchy inherit
'''

class school():
      def display_school(self):
            print("This is school class")
class teacher1(school):
      def display_teacher1(self):
            print("This is teacher1 class")
class teacher2(school):
      def display_teacher2(self):
            print("This is teacher2 class")
                                                               
class student(teacher1,teacher2):
      def display_student(self):
            print("This is student class")
            
s1=student()
s1.display_school()   
s1.display_teacher1()      
s1.display_teacher2()
s1.display_student()
                                         